from PIL import Image

def compress_image(default_image=Image.open('original_image.jpg')):
	''' Takes an image file and compress it without losing image quality. '''

	''' If no image file is provided, the default image will be compressed '''

	# Get image 'width' and 'height'
	w, h =  default_image.size
	# compress image
	default_image = default_image.resize((h, w), Image.ANTIALIAS)
	# return compressed image
	return default_image.save('compressed_image.jpg') 

# Run
compress_image()