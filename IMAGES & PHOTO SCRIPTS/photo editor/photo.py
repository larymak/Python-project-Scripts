from PIL import Image
me = Image.open('lary.png')
back = Image.open('images.jpg')
back.paste(me, (0,0), me)
back.show()















#me = Image.open('lary.png')
#bg = Image.open('images.jpg')
#bg.paste(me,(0,0),me)
#bg.show()