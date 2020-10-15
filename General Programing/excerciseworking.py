import os

from pydub import AudioSegment
from pydub.playback import play

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
    l =0
    for walert in walertlist:
        l +=1
        print(l)
        for alert in walert:
            if type(alert) == str :
                pathtovoice = PATH + "\walert{}".format(l) + "\\" + alert
                selected_voice = AudioSegment.from_file(pathtovoice, format='m4a')
                #time.sleep(30)
                play(selected_voice)



PATH = r'C:\Users\user\Documents\notification\workout'
walert1 = [i for i in os.listdir(PATH+"\walert1") if i.endswith(".mp3")]
walert2 = [i for i in os.listdir(PATH+"\walert2") if i.endswith(".mp3")]
walert3 = [i for i in os.listdir(PATH+"\walert3") if i.endswith(".mp3")]
walert4 = [i for i in os.listdir(PATH+"\walert4") if i.endswith(".mp3")]
walert5 = [i for i in os.listdir(PATH+"\walert5") if i.endswith(".mp3")]
walert6 = [i for i in os.listdir(PATH+"\walert6") if i.endswith(".mp3")]
walert7 = [i for i in os.listdir(PATH+"\walert7") if i.endswith(".mp3")]
walertlist = [walert1, walert2, walert3, walert4, walert5, walert6, walert7]
###
def excercise():
    l =0
    for walert in walertlist:
        l +=1
        for alert in walert:
            pathtovoice = PATH + "\walert{}".format(l) + "\\" + alert
            selected_voice = AudioSegment.from_file(pathtovoice, format='m4a')
            time.sleep(10)
            play(sound0)
            play(selected_voice)
            pathtosong =PATH + "\song{}.mp3".format(l//3+1)
            song = AudioSegment.from_mp3(pathtosong)
            play(song)
            # Pause other things and do this????????????????????????????????????
excercise()
