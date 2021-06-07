from captcha.audio import AudioCaptcha
from random import randint
audio = AudioCaptcha()
num = randint(100000,999999)
data = audio.generate(str(num))
audio.write(str(num), str(num)+'.mp3')
print(num)