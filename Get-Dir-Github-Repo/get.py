import argparse
import concurrent.futures
import fnmatch
import json
import sys
import os
import subprocess

__version__ = "1.1"


# This will attempt to import the modules required for the script run
# if fail to import it will try to install
modules = ['requests']

try:
    import requests
except:
    print('Attempting to install the requirements...')

    try:
        for module in modules:
            subprocess.run(['python', '-m', 'pip', 'install', module],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        import requests
        print('Requirements was successful installed!')
    except:
        try:
            for module in modules:
                subprocess.run(['python3', '-m', 'pip', 'install', module],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            import requests
            print('Requirements was successful installed!')
        except:
            sys.exit('Could not install requirements :(')


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
    """
    Check if the given url is valid and to ensure that get real repository information.
    """
    if url[-1] == "/":
        url = url[:-1]
    try:
        r = requests.head(url, timeout=30)
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
    else:
        if r.status_code == 404:
            sys.exit(
                "404: Verify internet connection or check if the url is correct")

        if not "https://github.com/" in url:
            sys.exit("Not a Github repo")

    user = url.split("/")[3]
    repo = url.split("/")[4]
    repo_api = f"https://api.github.com/repos/{user}/{repo}/contents"

    try:
        r2 = requests.get(repo_api, timeout=30)
        j = r2.json()

        if r2.status_code != 200:
            if r2.headers["content-type"] == "application/json; charset=utf-8":
                message = r.json()["message"]
                if type(message) == dict:
                    sys.exit(f"server: {message}")

        count = 0
        for token in range(0, len(j)):
            t = j[token]["type"]
            if t != "dir":
                count += 1
        if count == 0:
            sys.exit(f"No files found in {url}")

        else:
            return 0
    except requests.exceptions.RequestException:
        sys.exit(
            "Make sure you are provided a valid link and make sure you are connected to Internet."
        )


### End of functions ###


def Get(url):
    user = ""
    repo = ""
    path = ""

    if url[-1] == "/":
        url = url[:-1]

    try:
        sp = url.split("/")
        if len(sp) > 5:
            for _ in range(0, 7):
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
                r1 = r.status_code
                if r1 != 200:
                    if r.headers["content-type"] == "application/json; charset=utf-8":
                        if type(r.json()) == dict:
                            message = r.json()["message"]
                            if type(message) == dict:
                                sys.exit(f"server: {message}")
                    else:
                        sys.exit(f"{r1}: invalid url: {url}.")
            except requests.exceptions.RequestException:
                sys.exit(f"error: invalid url: {url}.")
    except:
        sys.exit(f"error: invalid url: {url}.")
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
    """
    Receives a list of dictionaries and a glob pattern list and it returns back a list
    with the files that match with each pattern and variable with the amount of matches.
    """
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
    r = requests.get(api_url, timeout=30).content.decode("utf-8")
except requests.exceptions.RequestException:
    sys.exit("error: Connetion error. Aborted.")

try:
    obj = json.loads(r)
    obj_len = len(obj)
except:
    sys.exit(f"error: Could not load files on {url}")


if include_list:
    print("Searching for matches...")
    (obj_, matches) = include(obj, include_list)

    if matches != 0:
        obj = obj_
        del obj_
        print(f"{matches} matches found to include")
    else:
        sys.exit(f"no matches for {include_list}")

if exclude_list:
    matches = search_pattern(obj, exclude_list)
    if matches:
        obj_ = exclude(obj, exclude_list, matches)
        obj = obj_
        del obj_
    else:
        print(f"{matches} matches found to ignore")

print(f"\nClonning into {directory}...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(fetch, obj)

print("\nDone")
