import pyttsx3
import time
import speech_recognition as sr
import wikipedia
import os
import random

import wish
import voice
import websites

if __name__ == '__main__':
        voice.speak(wish.wish())
        while True:
            query = voice.takeCommand()
            
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
            
            elif 'open' in query.lower():
                websites.open_website(query)
            
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
            
            elif 'open code' in query.lower():
                speak("Opening your VS code editor")
                vscode_path = r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                os.startfile(vscode_path)
                speak("Happy Hacking!")
    