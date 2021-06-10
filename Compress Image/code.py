import PIL
from PIL import Image

print("enter image name :")
image_name = str(input())  # image name with relative path

img = Image.open(image_name)
mywidth = img.size[0]
myheight = img.size[1]
img = img.resize((mywidth, myheight), PIL.Image.ANTIALIAS)
img.save("Resized_Image.jpeg")
