''' This module contains miscellaneous features of JARVIS '''

import datetime
import pyjokes
import random
import sys

import voice

thank_keys = ['thank you', 'thanks', "that's so sweet of you"]
thank_reply = ['No Problem', 'Happy to help', "That's what i am here for", "My plesure"]
bye_keys = ["Have a nice day", "Always here to serve", "Bye bye", "Ping me anytime"]

def misc(query):

    if 'time' in query.lower():
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        voice.speak(f"Current time is {str_time}")
    
    elif 'joke' in query.lower():
        joke = pyjokes.get_joke()
        voice.speak(joke)
    
    elif any([k in query.lower() for k in thank_keys]):
        voice.speak(random.choice(thank_reply))

    elif 'bye' in query.lower():
        voice.speak(random.choice(bye_keys))
        sys.exit()

    else:
        voice.speak("Aah man, what are you talking about?")