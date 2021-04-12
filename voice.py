''' This module handles JARVIS voice attributes'''

import pyttsx3
import speech_recognition as sr

mic = pyttsx3.init('sapi5')
voices = mic.getProperty('voices')
mic.setProperty('voice', voices[0].id)

def speak(audio):
    mic.say(audio)
    mic.runAndWait()

def takeCommand():
    '''Takes command/input from user's mic'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")  # Just for testing purposes

        except:
            print("Can you please say that again!")
            speak("Can you please say that again!")

            return "None"
        return query
