#!/usr/bin/env python3

from PIL import Image, ImageOps, UnidentifiedImageError
import sys, os

def check_input():
 """ Checks if the script is called with no input parameters. """
 if len(sys.argv) == 1:
  print("Please provide image files to operate on!")
  sys.exit(1)

def main():
 """ The main function """
 check_input()

 verbose_enabled = False
 if ("-v" in sys.argv)  or ("--verbose" in sys.argv):
  verbose_enabled = True

 i = 0
 for file in sys.argv:
  # To ignore the first parameter -> the script call + -v + --verbose
  if i == 0 or sys.argv[i] == "-v" or sys.argv[i] == "--verbose":
   i = i + 1
   continue

  image_path_no_ext, extension = os.path.splitext(file)

  try:
   with Image.open(file) as image:
    new_path_with_ext = image_path_no_ext + "_inverted" + extension
    ImageOps.invert(image).save(new_path_with_ext)
    if verbose_enabled:
     print("Successfully inverted " + file + "\n" + new_path_with_ext + " is generated.\n")
  except UnidentifiedImageError:
   print(file + " is not suppotred, please provide a supported file type.")
  i = i + 1

if __name__ == '__main__':
 main()
