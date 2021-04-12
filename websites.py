''' Open desired  websites '''

import webbrowser
import voice

def open_website(query):
    
    # Opening Wikipedia website
    if 'wikipedia' in query.lower():
        voice.speak("Opening wikipedia")
        webbrowser.open("wikipedia.com")
    
    # Opening Youtube website
    elif 'youtube' in query.lower():
        voice.speak("Opening Youtube!")
        webbrowser.open("youtube.com")
    
    # Google
    elif 'google' in query.lower():
        voice.speak("Opening google")
        webbrowser.open("Google")

    # Pragmatic programmer
    elif 'pragmatic programmer' in query.lower():
        voice.speak("Opeing Pragmatic programmer website")
        webbrowser.open("pragmaticprogrammer.in")

    # StackOverflow
    elif 'stack overflow' in query.lower():
        voice.speak("Opening Stack Over flow")
        webbrowser.open("stackoverflow.com")

    # GitHub
    elif 'github' in query.lower():
        voice.speak("Opening git hub!")
        webbrowser.open("github.com")
    
    # Netflix
    elif 'netflix' in query.lower():
        voice.speak(" opening netflix")
        webbrowser.open("netflix.com")
    
    else:
        voice.speak("Sorry, your desired website is not in my database!")