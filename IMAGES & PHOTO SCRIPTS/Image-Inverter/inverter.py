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

  file_name = os.path.splitext(file)
  try:
   with Image.open(file) as image:
    ImageOps.invert(image).save(filename + "_inverted", "JPEG")
  except:
   print("Couldn't convert " + filename + "successfully!")
  i = i + 1

if __name__ == '__main__':
 main()
