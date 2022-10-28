 # importing necessary libraries
import img2pdf
from PIL import Image
import os
  
# storing image path
img_path = "C:/Users/vedan/OneDrive/Desktop/image.png"
  
# storing pdf path
pdf_path = "C:/Users/vedan/OneDrive/Desktop/image.pdf"
  
# opening image
image = Image.open(img_path)
  
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
  
# opening or creating pdf file
file = open(pdf_path, "wb")
  
# writing pdf files with chunks
file.write(pdf_bytes)
  
# closing image file
image.close()
  
# closing pdf file
file.close()
  
# output
print("Successfully made pdf file")