""" Documentation Hub"""
import time
import datetime as dt

import os
from os.path import join
import random
import math


from pydub import AudioSegment
from pydub.playback import play

#####My appa##
from dailyactionlogs import *
from entertainmenthub import *
from excercisehub import *
from noteshub import *
from studieshub import *
from webscrapinghub import *

import traceback
def actionlog():
    sound0 = AudioSegment.from_mp3(r'C:\Users\user\Documents\notification\a.mp3')
    sound1 = AudioSegment.from_mp3(r'C:\Users\user\Documents\notification\notification5.mp3')
    sound2 = AudioSegment.from_mp3(r'C:\Users\user\Documents\Songs\Jesus-Lover-of-My-soul.mp3')
    #60*60*2
    i = 0
    start = time.time()
    stop = start + (3)
    while time.time() <= stop:
        try:
            entertainment()
            play(sound1)
            play(sound2)
            activity = input('Activity: ')
            description = input('Description')
            feeling = input('How do I feel about this work? ')
            datetime_object = dt.datetime.now()
            value = input('Give a rating on the value of this work High, Medium, Low, None):  ')
            activitylogs = open(r'C:\Users\user\Documents\Books Reading\activitylogs.txt', 'a+')
            activitylogs.write('{}, {}, {}, {} \n'.format(activity, description, datetime_object, value))
            activitylogs.close()
            sendmessage('25 minutes done! I have done {} \n, Description: {} \n, Date: {} \n, Value: {} \n'.format(activity, description, datetime_object, value), "My Messages")
            if input('Do you intend to keep working? ').lower()== 'yes':
                continue
            else:
                break
        except:
            traceback.print_exc()
            break

if __name__ == "__main__":
    actionlog()
