import pyttsx3               #import pyttsx3 module
engine = pyttsx3.init()      #pyttsx3.init() factory function to get a reference to a pyttsx3.Engine instance
engine.say('Hello World')
engine.say('Hello GitHub')
engine.say('Hello Python Project Scripts')
engine.runAndWait()
