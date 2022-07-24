#!/usr/bin/env python3

from PIL import Image
from PIL import ImageOps
import sys, os

def main():
 # if the script is called with no input
 if len(sys.argv) == 1:
  print("Please provide files to operate on!")
  sys.exit(1)

 i = 0
 for file in sys.argv: 
  # ignore the first parameter -> the script call
  if i == 0:
   i = i + 1
   continue

  image_path, extension = os.path.splitext(file)

  with Image.open(file) as image:
   ImageOps.invert(image).save(image_path + "_inverted" +  extension, "JPEG")

  i = i + 1

if __name__ == '__main__':
 main()
