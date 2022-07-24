#!/usr/bin/env python3

from PIL import Image
from PIL import ImageOps
import sys, os

def check_input():
 """ Checks if the script is called with no input parameters. """
 if len(sys.argv) == 1:
  print("Please provide image files to operate on!")
  sys.exit(1)

def main():
 """ The main function """
 check_input()

 i = 0
 for file in sys.argv:
  # To ignore the first parameter -> the script call
  if i == 0:
   i = i + 1
   continue

  image_path_no_ext, extension = os.path.splitext(file)

  with Image.open(file) as image:
   ImageOps.invert(image).save(image_path_no_ext + "_inverted" +  extension)

  i = i + 1

if __name__ == '__main__':
 main()
