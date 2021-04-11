import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random



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
    
    speak("Jarvis here! How can I help you?")


def takeCommand():
    '''Takes command/input from user's microphone'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
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
        wish()
        while True:
            query = takeCommand()
            
            # Wikipedia
            if 'wikipedia' in query.lower():
                speak("Searching wikipedia")
                
                try:
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    speak(results)
                except:
                    speak("No result found on wikipedia!")
            
            # Youtube
            elif 'open youtube' in query.lower():
                speak("opening youtube")
                time.sleep(1)
                webbrowser.open("youtube.com")
                speak("Youtube is here!")

            # Google
            elif 'open google' in query.lower():
                speak("opening google")
                time.sleep(1)
                webbrowser.open("google.com")
                speak("Google is here!")
            
            # Pragmatic Programmer
            elif 'open pragmatic programmer' in query.lower():
                speak("Opening your website")
                time.sleep(1)
                webbrowser.open("pragmaticprogrammer.in")
                speak("Pragmatic Programmer's website is here.")

            # Stack Overflow
            elif 'open stack overflow' in query.lower():
                speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")
                speak("Stackoverflow is here!")
            
            elif 'play' in query.lower() and 'music' in query.lower():
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                song = random.randint(0, len(songs) - 1)
                print(f"Playing {songs[song]}")
                speak(f"Playing {songs[song]}")
                os.startfile(os.path.join(music_dir, songs[song]))
            
            elif 'the time' in query.lower():
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"time: {str_time}")
                speak(f"Current time is {str_time}")
