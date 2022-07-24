#!/usr/bin/env python3

from PIL import Image
from PIL import ImageOps
import sys, os

def main():
 if len(sys.argv) == 1:
  print("Please provide files to operate on!")
  sys.exit(1)

 for file in sys.argv: # TODO: remove the sys.argv[0] from the loop! use index i and start from 1
   # TODO: add a check that the files are jpg
  file_name = os.path.splitext(file)
  with Image.open(file) as image:
   inverted_image = ImageOps.invert(image)
   inverted_image.save(filename + "_inverted", "JPEG")
 
 sys.exit(0)

if __name__ == '__main__':
 main()
