from PIL import Image
from os import listdir,getcwd
from os.path import isfile, join

onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
print("All files in current dir :",onlyfiles)

img = Image.open(input("Enter image filename : "))  # image name with relative path
grayscale = img.convert('L')
grayscale.save('GrayScaled_{}'.format(img.filename))

