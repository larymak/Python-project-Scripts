from tkinter import Tk
from tkinter.filedialog import askdirectory
import os, hashlib
from pathlib import Path


Tk().withdraw()  # to hide the small tk window
path = askdirectory(title='Select Folder')  # shows dialog box and return the path

files_list = os.listdir(path)  # take all the filename as a list

unique = dict()  # making a dictionary named unique

for file in os.listdir(path):   # looping over the file list

    file_name = Path(os.path.join(path, file))  # make a absolute file name using os.path.join function
    if file_name.is_file():  # checking the the the item is file or not

        fileHash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()
        if fileHash not in unique:
            unique[fileHash] = file_name

        else:
             print(file_name)
             os.remove(file_name)
        print(f" File will be deleted {file_name}")
    else:
        print("Path not exits")
