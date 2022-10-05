from PIL import Image
import os

def compress_image():
    ''' Takes an image file and compress it without losing image quality. '''

    ''' If no image file is provided, the default image will be compressed '''
    try:
        image_name = str(input("Enter the name of the image you want to compress: "))
        default_image=Image.open(f'{image_name}')
    except FileNotFoundError:
        default_image=Image.open('original_image.jpg')
            
    # Get image 'width' and 'height'
    w, h =  default_image.size
    # Separate the file name from the extension
    default_image_name = os.path.splitext(os.path.basename(default_image.filename))
    # compress image
    default_image = default_image.resize((w, h), Image.ANTIALIAS)
    # return compressed image
    return default_image.save('{}_compressed{}'.format(default_image_name[0], default_image_name[1]))

# Run
compress_image()
