# Extract text from images in a given directory

## Description
This script will extract the text from images in a specified directory and store the output in a given .txt file. The .txt file will contain the text contents of the images in order of their presence in the given directory.

## Requirements

`$ pip install Pillow`
`$ pip install pytesseract`
 
Download and install the required tesseract.exe file here: https://osdn.net/projects/sfnet_tesseract-ocr-alt/downloads/tesseract-ocr-setup-3.02.02.exe/

## Steps To Execution
- Fork this repo and navigate to Extract Text From Image folder in local folder
- Edit `image-text.py` with the string for the images directory.
- Run this code like so; `$ python image-text.py`
- In a short bit you'd have the .txt file with the texts extracted
- Enjoy and goodluck on your freelancing copy-typing jobs! (how the script idea came to be. Really couldn't type out text in TONS of image files lol)

## Code Output
`"IMAGE_TITLE" done` for each image in directory when text extraction is complete for said image
`Text extract script completed!` - at the end of the script.

Hit `Ctrl-C` to exit script.