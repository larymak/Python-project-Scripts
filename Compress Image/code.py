from PIL import Image
img =  Image.open('1.jpg')  ## file name of relative path with file name (with extension)
h,w =  img.size   ## getting height and width of image
img = img.resize((h,w),Image.ANTIALIAS)   ## compression
img.save('1_compressed.jpg')  ## output location and file name 
print("Image Compression Process Successfully Completed !! ")