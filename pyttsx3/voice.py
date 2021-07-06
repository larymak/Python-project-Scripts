#This Example based on Saving voice to a file

import pyttsx3                        #import pyttsx3
engine = pyttsx3.init()
engine.save_to_file('Hello World' , 'test.mp3')  #saving voice to file
engine.runAndWait() 
