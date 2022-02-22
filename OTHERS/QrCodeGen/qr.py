import qrcode

image = qrcode.make(input("Write Your message: "))
image.save("subscribe.jpg")