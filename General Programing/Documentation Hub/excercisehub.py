""" Documentation Hub"""
import time
import datetime as dt

import threading

import os
from os.path import join
import random

import pyglet

from pydub import AudioSegment
from pydub.playback import play


import traceback
########
PATH = r'C:\Users\user\Documents\notification\workout'
walert1 = [i for i in os.listdir(PATH+"\walert1") if i.endswith(".m4a")]
walert2 = [i for i in os.listdir(PATH+"\walert2") if i.endswith(".m4a")]
walert3 = [i for i in os.listdir(PATH+"\walert3") if i.endswith(".m4a")]
walert4 = [i for i in os.listdir(PATH+"\walert4") if i.endswith(".m4a")]
walert5 = [i for i in os.listdir(PATH+"\walert5") if i.endswith(".m4a")]
walert6 = [i for i in os.listdir(PATH+"\walert6") if i.endswith(".m4a")]
walert7 = [i for i in os.listdir(PATH+"\walert7") if i.endswith(".m4a")]
walertlist = [walert1, walert2, walert3, walert4, walert5, walert6, walert7]
###
def excercise():
    sound0 = AudioSegment.from_mp3(r'C:\Users\user\Documents\notification\a.mp3')
    sound1 = AudioSegment.from_mp3(r'C:\Users\user\Documents\notification\notification5.mp3')
    sound2 = AudioSegment.from_mp3(r'C:\Users\user\Documents\Songs\Jesus-Lover-of-My-soul.mp3')
    sound3 =  "Workout.mp4"
    l =0
    def thesong():
        music = pyglet.resource.media(sound3)
        music.play()
        music.volume = .5
        pyglet.app.run()
    t1 = threading.Thread(target = thesong)
    t1.start()
    time.sleep(3)
    for walert in walertlist:
        l +=1
        print("Start Phase.... {}".format(l))
        for alert in walert:
            pathtovoice = PATH + "\walert{}".format(l) + "\\" + alert
            selected_voice = AudioSegment.from_file(pathtovoice, format='m4a')
            play(sound0)
            if walert == walert6:
                for i in range(4):
                    time.sleep(1)
                    play(selected_voice)
                    alertnumber = alert.split(" ")[1]

                    if alertnumber == "000":
                        print("Almost Done")
                    else:
                        print("Start Phase.... {}".format(l))
                        #pathtosong =PATH + "\song{}.mp3".format(l//3 +1)
                        #song = AudioSegment.from_mp3(pathtosong)
                        time.sleep(30)
            else:
                time.sleep(1)
                play(selected_voice + 3)

                alertnumber = alert.split(" ")[1]

                if alertnumber == "000":
                    print(" ")
                else:
                    print("pass")
                    time.sleep(30)
            # Pause other things and do this????????????????????????????????????
if __name__ == "__main__":
 excercise()
 # There are bugs: delays in playing songs, some alerts are missing: switch sides at last phase.
