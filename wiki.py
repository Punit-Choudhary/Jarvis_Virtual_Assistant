''' Module to search on wikipedia '''

import wikipedia
import voice

def search(query):
    voice.speak("Searching on wikipedia")
    try:
        query = query.replace('Wikipedia', '')

        results = wikipedia.summary(query, sentences=2)
        print(results) # for testing purpose only
        voice.speak(f"According to wikipedia, {results}")
    
    except:
        voice.speak("No result found on wikipedia!")
