import os
from os.path import join
import random
import math

from docx import Document
from docx.shared import Inches

from pydub import AudioSegment
from pydub.playback import play

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import traceback


def entertainment():
    PATH = r"C:\Users\user\Music"
    songs = []
    for root, dirs, files in os.walk(PATH+"\\all"):
        songs.append([join(root, name) for name in files if name.endswith(".mp3")])
    while True:
        try:
            pathtosong = random.choice(songs[0])
            selected_song = AudioSegment.from_mp3(pathtosong)
            sliced = selected_song[7000:] # get a slice from 5 to 10 seconds of an mp3
            play(selected_song)
        except:
            print("problem occurred")
            break

if __name__ == "__main__":
 entertainment()
