import imp
#import important libraries

import os 
import pytesseract as py
from PIL import Image

# receive image and extract text
def extract_text(img_path):
    image = Image.open(img_path)
    text = py.image_to_string(image)
    return text 


if __name__ == '__main__':
    image_path = input('Enter image: ')
    print(extract_text(image_path))


    