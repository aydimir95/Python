"""
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
"""

from gtts import gTTS
import os
import cowsay

this = input("What's this? ")
cowsay.cow(this)

tts = gTTS(text=this, lang="en")
tts.save("output.mp3")
os.system("mpg321 output.mp3")