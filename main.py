import pyttsx3
import time
import speech_recognition as sr
import pyjokes

import wish
import voice
import websites
import wiki
import song
import application
import weather
import news
import misc

if __name__ == '__main__':
        voice.speak(wish.wish())
        while True:
            query = voice.takeCommand()
            
            
            if 'open' in query.lower():
                websites.open_website(query)
            
            elif 'wikipedia' in query.lower():
                wiki.search(query)

            elif 'play' in query.lower() and 'music' in query.lower():
                song.play()

            elif 'start' in query.lower():
                application.start(query)
            
            elif 'weather' in query.lower():
                weather.fetch_weather()
            
            elif 'news' in query.lower():
                news.get_news()
            
            elif 'None' not in query:
                misc.misc(query)
