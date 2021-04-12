''' This module will play songs '''

import os
import random
import voice

music_dir = r"D:\music"
songs = os.listdir(music_dir)

def play():
    song = random.randint(0, len(songs) - 1)
    print(f"Playing: {songs[song]}") # for testing purpose only
    voice.speak(f"Playing {songs[song]}")

    os.startfile(os.path.join(music_dir, songs[song]))
