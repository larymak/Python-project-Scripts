from captcha.image import ImageCaptcha
from random import randint

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

num = random_with_N_digits(int(input("Enter number of digits:")))
name = ("%d.png" % num)
image = ImageCaptcha()
data = image.generate("'%d'" % num)
image.write("'%d'" % num, name)
print("A {}.png is generated".format(num))