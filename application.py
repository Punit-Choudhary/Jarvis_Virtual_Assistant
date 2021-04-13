''' This module will start installed applications '''

import os
import voice

def start(query):

    # VS code
    if 'code' in query.lower() or 'vs code' in query.lower():
        vscode_path = r"C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(vscode_path)
        voice.speak("Happy Hacking!")

    # Spotify
    elif 'spotify' in query.lower():
        spotify_path = r"C:\Users\Admin\AppData\Roaming\Spotify\Spotify.exe"
        os.startfile(spotify_path)
        voice.speak("Chill")
    
    # Chrome
    elif 'chrome' in query.lower():
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        os.startfile(chrome_path)
        voice.speak("I have opened chrome browser")
    
    # Internet Explorer
    elif 'internet explorer' in query.lower():
        voice.speak("Do you really want to open Internet Explorer")
        query = voice.takeCommand()

        if 'yes' in query.lower():
            explorer_path = r"C:\Program Files\Internet Explorer\iexplore.exe"
            os.startfile(explorer_path)
            voice.speak("Here comes world's best browser......to download other browsers")
            voice.speak("hahaha")
        else:
            voice.speak("good choice")
            voice.speak("so, is there any job for me?")

    # Sumblime text editor
    elif 'sublime' in query.lower():
        sublime_path = r"E:\Installed Softwares\Sublime Text 3\sublime_text.exe"
        os.startfile(sublime_path)
        voice.speak("Done")

    # BlueStack
    elif 'bluestack' in query.lower():
        bluestack_path = r"C:\Program Files\BlueStacks\Bluestacks.exe"
        os.startfile(bluestack_path)
        voice.speak("Here comes your emulator!")
    
    # Discord
    elif 'discord' in query.lower():
        discord_path = r"C:\Users\Admin\AppData\Local\Discord\Update.exe --processStart Discord.exe"
        os.startfile(discord_path)
        voice.speak("Here you go...")
