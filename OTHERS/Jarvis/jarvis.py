from email.mime import audio
from importlib.resources import path
from logging import exception
from random import Random, random
from re import S
import sys
from typing_extensions import Self
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# wish function
def wish():
    hour = int(datetime.datetime.now().hour)
    #tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour <= 12:
        speak("Good morning,sir")
    elif hour > 12 and hour < 18:
        speak("Good afternoon,sir")
    else:
        speak("Good Evening,sir")
    speak("I am Jarvis sir,How can I help you?")


# to define send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vedantgaikwad@gmail.com', 'Tata@1234')
    server.sendmail('vedantgaikwad@gmail.com', to, content)
    server.close()

# to convert voice  into text
class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    def takecommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=2, phrase_time_limit=5)

        try:
            print("Recognizng..")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except exception as e:
            speak("could you please repeat...")
            return "none"
        query = query.lower()    
        return query

    #if __name__ == "__main__":
    def TaskExecution(self):
    #def start():
        wish()

        while True:

            self.query = self.takecommand()

            # logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 10.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.inshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                music_dir = "C:\\Users\\vijay\\Music"
                songs = os.listdir(music_dir)
                rd = Random.choice(songs)
                # for song in songs:
                #   if song.endswith('.mp3'):
                os.startfile(os.path.join(music_dir, rd))
                # os.startfile(os.path.join(music_dir,song))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP Address is {ip}")

            elif "wikipedia" in self.query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentence=2)
                speak("According to wikipedia")
                speak(result)
                # print(result)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stack overflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                # to search something specific on google
                speak("Sir what should i search on google")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")

            elif "send message" in self.query:
                #speak("Sir,to whom should i send message")
                #wmsg = takecommand().lower()
                # 2.25 is time at which you send
                kit.sendwhatmsg("+919920309439", "this is a testing message", 2.25)

            elif "play songs on youtube" in self.query:
                speak("Sir what should i play on youtube")
                play = self.takecommand()
                kit.playonyt(f"{play}")

            elif "send email" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand()
                    to = "sanjayg1973@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")

                except exception as e:
                    print(e)
                    speak("sorry sir, i am not able to send the email")

            # to close application
            elif "close notepad" in self.query:
                speak("okay sir,closing notepad")
                os.system("taskkill /f/im notepad.exe")

            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 11:
                    music_dir = "Libraries\\Music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "thank you" in self.query:
                speak("thankyou sir,have a good day")
                sys.exit()

            speak("sir,do you have any other work")



#if __name__ == "__main__" :
#    TaskExecution()

startExecution = Mainthread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        #self.ui.movie = QtGui.QMovie("Black_Template.jpg")
        #self.ui.label.setMovie(self.ui.movie)
        #self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Iron_Template_1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("jarvis_jj.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("initial.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Health_Template.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("B.G_Template_1.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date =  current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())





