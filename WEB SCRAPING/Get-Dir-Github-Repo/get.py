import argparse
import concurrent.futures
import fnmatch
import sys
import os
import subprocess
from itertools import product

__version__ = "1.1"


# This will attempt to import the modules required for the script run
# if fail to import it will try to install
modules = ["requests"]

try:
    import requests
except:
    print("Attempting to install the requirements...")

    try:
        for module in modules:
            subprocess.run(
                ["python", "-m", "pip", "install", module],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        import requests

        print("Requirements was successful installed!")
    except:
        try:
            for module in modules:
                subprocess.run(
                    ["python3", "-m", "pip", "install", module],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            import requests

            print("Requirements was successful installed!")
        except:
            sys.exit("Could not install requirements :(")


### Comandline arguments ###
parser = argparse.ArgumentParser(
    description="Single Github repository directory downloader.",
    usage="%(prog)s [<optional arguments>] <url> [<destination>]",
)
parser.add_argument(
    "url",
    nargs=1,
    help="Github repository url, example: https://github.com/[<owner>]/[<repo>]",
)
parser.add_argument(
    "-V", "--version", action="version", version=f"%(prog)s {__version__}"
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Print each file of the repository while clonnig",
)
parser.add_argument(
    "-I",
    "--include-only",
    dest="include",
    nargs=1,
    help="Include only the files that match the given glob pattern.",
)
parser.add_argument(
    "-E", "--exclude", nargs=1, help="Exclude files that match the given glob pattern."
)
parser.add_argument(
    "output",
    nargs="?",
    default=None,
    help="Name of the directory to clone into. (Default is branch name)",
)

if len(sys.argv) == 1:
    parser.print_help()

args = parser.parse_args()


### Functions ###
def check_url(url):
    if not "https://github.com/" in url:
        sys.exit("The url must to be a valid and public Github repository.")

    if url[-1] == "/":
        url = url[:-1]

    try:
        r = requests.get(url, timeout=30)
    except requests.ConnectionError as e:
        print(
            "OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n"
        )
        sys.exit(str(e))
    except requests.Timeout as e:
        print("OOPS!! Timeout Error")
        sys.exit(str(e))
    except requests.RequestException as e:
        print("OOPS!! General Error")
        sys.exit(str(e))
    except KeyboardInterrupt:
        sys.exit("Someone closed the program")

    if r.status_code == 404:
        sys.exit(f"404 Client Error: Not Found for url: {url}")


def Get(url):
    user = ""
    repo = ""
    path = ""

    if url[-1] == "/":
        url = url[:-1]

    try:
        sp = url.split("/")
        if len(sp) > 5:
            for _ in range(7):
                sp.pop(0)
            path = "/".join(sp)

        user = url.split("/")[3]
        repo = url.split("/")[4]
        if path:
            api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
        else:
            api_url = f"https://api.github.com/repos/{user}/{repo}/contents"

        if api_url:
            try:
                r = requests.get(api_url, timeout=30)
                code = r.status_code

                if code == 403:
                    if r.headers["content-type"] == "application/json; charset=utf-8":
                        if "message" in r.json():
                            sys.exit("You reached requests limit, try again later!")
                if code == 404:
                    sys.exit(f"error: {code}")
            except requests.exceptions.RequestException as e:
                sys.exit(f"error:\n{e}")
        else:
            sys.exit(f"error: could not extract information about repo: {url}.")
    except Exception as e:
        print(e)
        sys.exit(f"error: could not extract information about repo: {url}.")
    else:
        return {"api_url": api_url, "repo": repo, "path": path}


def search_pattern(obj, pattern_list):
    matches = 0
    for token in range(0, len(obj)):
        f = obj[token]["name"]
        for p in pattern_list:
            if fnmatch.fnmatch(f, p):
                matches += 1

    return matches


def include(obj, pattern_list):
    include_list = []
    matches = 0

    for index in range(0, len(obj)):
        f = obj[index]["name"]
        t = obj[index]["type"]
        if t != "dir":
            for p in pattern_list:
                if fnmatch.fnmatch(f, p):
                    include_list.append(obj[index])
                    matches += 1

    return (include_list, matches)


def exclude(obj, pattern_list, matches):
    count = 0
    while matches != 0:
        for _ in obj:
            l = len(obj)
            if count == l:
                count = 0

            f = obj[count]["name"]
            for p in pattern_list:
                if fnmatch.fnmatch(f, p):
                    # print(f'{f}, {count}')
                    obj.pop(count)
                    matches -= 1
            count += 1

    return obj


def fetch(obj):
    file = obj["name"]
    url = obj["download_url"]

    content = requests.get(url).content
    filename = os.path.join(directory, file)
    f = open(filename, "bw")
    f.write(content)
    f.close()

    if verbose:
        print(file)


url = args.url[0]
check_url(url)

verbose = args.verbose
output = args.output
api_url = Get(url)["api_url"]
repo = Get(url)["repo"]
path = Get(url)["path"]
include_list = args.include
exclude_list = args.exclude
directory = ""

if include_list and exclude_list:
    # Check if the glob patttern given to -I and -E
    # was the same, if it is exit with an error
    globs = list(product(include_list, exclude_list))
    for token in range(len(globs)):
        i = globs[token][0]
        e = globs[token][1]

        if i == e:
            print(f"-I and -E cannot share same glob pattern: {i}")
            sys.exit(0)

if output:
    directory = output
else:
    directory = repo

if path:
    directory = os.path.join(directory, path)

if os.path.isdir(directory):  # Check is directory exist.
    if any(os.scandir(directory)):  # is it empty?
        sys.exit(f"'{directory}' already exist and is not empty.")
else:
    try:
        os.makedirs(directory)
    except:
        sys.exit(f"Could not create '{directory}'.")

r = ""

try:
    r = requests.get(api_url, timeout=30)
except requests.exceptions.RequestException:
    sys.exit("error: Connetion error. Aborted.")

try:
    obj = r.json()
    obj_len = len(obj)
except:
    sys.exit(f"error: Could not load files on {url}")


if include_list:
    print("Searching for matches...")
    (obj_, matches) = include(obj, include_list)

    if matches != 0:
        obj = obj_
        print(f"{matches} matches found to include")
    else:
        sys.exit(f"no matches for {include_list}")

if exclude_list:
    matches = search_pattern(obj, exclude_list)
    if matches:
        obj_ = exclude(obj, exclude_list, matches)
        obj = obj_
    else:
        print(f"{matches} matches found to ignore")

print(f"\nClonning into {directory}...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fetch, obj)

print("\nDone")
