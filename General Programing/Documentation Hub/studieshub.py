""" Documentation Hub"""
import time
import datetime as dt

import os
from os.path import join
import random
import math

from docx import Document
from docx.shared import Inches

from pydub import AudioSegment
from pydub.playback import play

import traceback

import voices
import clipboard
import pyperclip as pc
text2 = pc.paste().rstrip("\n")

import math



##My apps
from noteshub import *
from webscrapinghub import *
sound0 = AudioSegment.from_mp3(r'C:\Users\user\Documents\notification\a.mp3')
sound1 = AudioSegment.from_mp3(r'C:\Users\user\Documents\notification\notification5.mp3')
sound2 = AudioSegment.from_mp3(r'C:\Users\user\Documents\Songs\Jesus-Lover-of-My-soul.mp3')
start = time.time()
def recordnotes():
    book = input('Enter the book that you read: ')
    description = input('Description: What chapter? What page? ')
    feeling = input('Reflection: How do I feel about this book? ')
    datetime_object = dt.datetime.now()
    value = input('Give a rating on the value of this reading High, Medium, Low, None):  ')
    readinglogs = open(r'C:\Users\user\Documents\Books Reading\reading.txt', 'a+')
    readinglogs.write('{}, {}, {}, {} \n'.format(book, description, datetime_object, value))
    readinglogs.close()
    #Estimate time when the book will be finished
    pagesunread = int(input('How many pages of the book did you read Remains? '))
    pagesread = float(input('How many pages of the book did you read? '))
    rate_of_reading = 25/pagesread
    remaining_time = math.ceil((rate_of_reading*pagesunread)/360)
    smessage = '25 minutes done! I read {}:\n   -Description: {}.\n  -Date: {}.\n    -Value: {}.\n   -It might take you {} days to finish for 6 hour reading a day'.format(book, description, datetime_object, value, remaining_time )
    print(smessage)
    notes()
    
def studytrack():
    print("studying.................")
    i = 0
    while True:
        voiceassistant = input("Would youwant to get assistant? ")
        if voiceassistant == "yes":
            input("Copy and press Enter! ")
            voices.readtext(text2)
            endtime = time.time()
            timespend = (endtime- start)//60
            nextread = input("Enter for Next, Q for quit")
            if nextread == "":
                studytrack()
            else:
                text = "You spend {} minutes".format(timespend)
                print(text)
                clipboard.copy(text)
                voices.readtext(text)
                recordnotes()
        else:
            play(sound1)
            
            i = i + 1
            time.sleep(5*60)
            if i ==1:
                print(i*5, " Minute Spend")
            else:
                print(i*5 , " Minutes Spend")
                try:
                    if i*5 % 120 == 0:
                        recordnotes()
                        play(sound2)
                    else:
                        play(sound1-3)
                except:
                    traceback.print_exc()
if __name__ == "__main__":
 studytrack()
