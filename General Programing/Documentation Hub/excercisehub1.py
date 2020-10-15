""" Documentation Hub"""
import time
import datetime as dt
import winsound
import os
from os.path import join
import random
#startfile(r"C:\Users\user\Music\all\Workout.mp4")
###
def excercise():
    l = 0
    for walert in list(range(7)):
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
                        pathtosong =PATH + "\song{}.mp3".format(l//3 +1)
                        song = AudioSegment.from_mp3(pathtosong)
                        play(song)
            else:
                time.sleep(1)
                play(selected_voice)

                alertnumber = alert.split(" ")[1]

                if alertnumber == "000":
                    print("Let's Start")
                else:
                    print("pass")
                    pathtosong =PATH + "\song{}.mp3".format(l//3 +1)
                    song = AudioSegment.from_mp3(pathtosong)
                    play(song)
            # Pause other things and do this????????????????????????????????????
if __name__ == "__main__":
 excercise()
 # There are bugs: delays in playing songs, some alerts are missing: switch sides at last phase.
