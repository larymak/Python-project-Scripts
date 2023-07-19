import os
import shutil

from contextlib import contextmanager
from pathlib import Path


@contextmanager
def copy_work(working_dir, text_to_replace, replacement_text):
    """
    Recursive function that iterates down through source directory until a file is reached. If file is newer than same
    file in the target directory then replaces target file with source version. If source doesn't exist in target
    directory then copies source file into target directory.
    :param replacement_text: replacement text to put into source path i.e /a/b/<replacement_text>/file
    :param text_to_replace: text that needs to be replaced in source path i.e /a/b/<text_to_replace>/file
    :param working_dir: the source directory that contains the newest files.
    :return: copied file
    """
    os.chdir(working_dir)
    for file in Path.cwd().iterdir():
        if file.is_file():
            try:
                p1, p2 = os.path.getmtime(Path(file.as_posix())), os.path.getmtime(Path(
                    f'{os.path.split(file.as_posix())[0].replace(text_to_replace, replacement_text)}/{os.path.split(file.as_posix())[1]}').as_posix())
                if p1 > p2:
                    shutil.copy(Path(file).as_posix(), Path(
                        f'{os.path.split(file.as_posix())[0].replace(text_to_replace, replacement_text)}/{os.path.split(file.as_posix())[1]}'))
                    print(f'{Path(file).name} replaced.')
            except:
                shutil.copy(Path(file).as_posix(), Path(
                    f'{os.path.split(file.as_posix())[0].replace(text_to_replace, replacement_text)}/{os.path.split(file.as_posix())[1]}'))
                print(f'{Path(file).name} added.')
        else:
            copy_work(file, text_to_replace, replacement_text)

