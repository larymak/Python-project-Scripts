# Have you ever thought how do I download just a subdirectory from a Github repository? Yes? So this is the solution!

*Get* (I should take a better name..) is a *"multithreaded"* python script for dealing with a common problem that sometimes I pass through, get just some files from a repo whithou having to clone the whole repo.

## Installation

1. Download [get.py](https://raw.githubusercontent.com/larymak/Python-project-Scripts/main/Get-Dir-Github-Repo/get.py).

## Requirements
The script will check if the required modules are installed, if not it will try install them. If it fails, you will have to manually install them. Get.py for now only have one module that not comes with python by default, *Requests*. *__Make sure you have python 3 proprely installed on your system.__*

Download [requirements.txt](https://raw.githubusercontent.com/larymak/Python-project-Scripts/main/Get-Dir-Github-Repo/requirements.txt) and run:

```
python3 -m pip install -r requirements.txt
```

## Usage
```cmd
python3 get.py [URL] [OPTIONAL ARGS]
```
Let's say you want get some files from a repo: *https://github.com/user/repo*.
```
repo/
  test/
  build/
  src/
  file1.py
  file2.py
  file3.py
  file4.py
  file5.py
  file6.py
  file.json
  file.yaml
  README.md
  .gitiginore
```
When providing a valid and public github repository, the script will get the files that list on the current directory get from the url, all subdirectories will be ignored.

```cmd
python3 get.py https://github.com/user/repo
```
A directory with the name of the repo will be create on working directory on your file system:
```
repo/
  file1.py
  file2.py
  file3.py
  file4.py
  file5.py
  file6.py
  file.json
  file.yaml
  README.md
  .gitiginore
```
### If I want filter the files?
No problem, you can use the flags *--include-only or -I and --exclude or -E* for filter the files you want and don't want with glob search pattern.

```cmd
python3 get.py https://github.com/user/repo -I *.py
```
```cmd
python3 get.py https://github.com/user/repo -E *.md .*
```
#### For more information run:
```cmd
python3 get.py --help
```

