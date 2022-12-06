#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(description="Take a directory path or a filename and calculate those sizes in KB")
# Creating an ArgumentParser object

parser.add_argument("-F", help="Choose file prefix for recursive search in directory")
parser.add_argument("path", help="File or directory path for calculating size")
# Adding arguments

group = parser.add_mutually_exclusive_group()
# Creating MutuallyExclusiveGroup object

group.add_argument("-d", action="store_true", help="Directory name for calculate size in KB")
group.add_argument("-f", action="store_true", help="File name for calculate file size in KB")
# Adding mutually exclusive arguments [-d | -f]

args = parser.parse_args()
# Taking arguments from command line

F_argument = args.F
d_argument = args.d
f_argument = args.f
path = args.path
# Unpacking arguments to variables

is_dir = os.path.isdir(path)
# Check if path is a directory not a file

if F_argument and not d_argument and not f_argument:
    # If user uses [-F] option lonely
    print('[-F] option cannot be used alone')

elif d_argument and is_dir and not f_argument and not F_argument:
    # If [-d] used and path is a directory

    def get_size(start_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp) / 1024
                    # Calculate files sizes and convert to kb

        return total_size


    print(f"Size of files in directory: {get_size(path):.3f} KB")

elif d_argument and not is_dir and not f_argument and not F_argument:
    # If user uses -d option with a file path not a directory
    print('Must use a directory path with [ -d ].')

elif f_argument and not is_dir and not d_argument and not F_argument:
    # Id [-f] option used and a file name was entered
    file_size = os.path.getsize(path) / 1024
    # Calculate file size and convert to kb
    print(f"Size of file {path} is: {file_size:.3f} KB")

elif f_argument and is_dir and not d_argument and not F_argument:
    # If user uses [-f] option with a directory path not a file path
    print('Must use [ -f ] with a file name not a directory path')

elif f_argument and F_argument:
    # If user uses [-F] option with [-F] option
    print('You can not use [-F] option with [-f] option')

elif F_argument and d_argument and is_dir and not f_argument:
    # If [-F] for search files with their prefixes in a [-d] directory
    def get_size(start_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                if f.endswith(F_argument):
                    fp = os.path.join(dirpath, f)
                    # skip if it is symbolic link
                    if not os.path.islink(fp):
                        total_size += os.path.getsize(fp) / 1024
                        # Calculate files sizes and convert to kb

        return total_size


    print(f"Size of {F_argument} files in directory: {get_size(path):.3f} KB")

elif F_argument and d_argument and not is_dir and not f_argument:
    # If user uses [-F] option and [-d] option and a file path except directory path
    print('Must use [ -d ] option with a directory path')
