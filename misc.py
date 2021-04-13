''' This module contains miscellaneous features of JARVIS '''

import datetime
import pyjokes

import voice


def misc(query):

    if 'time' in query.lower():
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        voice.speak(f"Current time is {str_time}")
    
    elif 'joke' in query.lower():
        joke = pyjokes.get_joke()
        voice.speak(joke)
    else:
        voice.speak("Aah man, what are you talking about?")