from gtts import gTTS
from playsound import playsound

audio='speech.mp3'
playsound(audio)
lang='en'
text="hELLO, OPEN SOURCE!"
sp=gTTS(text=text,lang=lang,slow=False)
sp.save(audio)
