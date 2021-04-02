import pyttsx3
import datetime
import time
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    '''Wish to user, depending upon time!'''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    
    time.sleep(1)
    speak("Jarvis here! How can I help you?")


def takeCommand():
    '''Takes command/input from user's microphone'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        
        except Exception as e:
            print("Can you please say that again")
            speak("Can you please say that again!")
            return "None"
    return query


if __name__ == '__main__':
        #to_speak = input("Enter text: ")
        #peak(to_speak)
        wish()
        while True:
            takeCommand()
            time.sleep(2)