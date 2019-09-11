# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:35:45 2019

@author: Sayak
"""

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Say Something")
    audio = r.listen(source)
    print ("Time is Over")

try:
    print("Text:-" + r.recognize_google(audio))
except:
    pass
