import numpy as np
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

import openpyxl

from selenium import webdriver


import time

import webscrapinghub

# python -m pip install plyer
from plyer import notification
def notifyme(tl, msg):
    notification.notify(
        title= tl,
        message= msg,
        app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
        timeout=10,  # seconds
        )


def gamequery(soccer_containers):
    gamedict = {}
    for i in range(len(soccer_containers)):
        leagueinfo = soccer_containers[i].find_all('div', class_ = "teams-info-meta-left")[0].text.strip().split("                         - ")
        timeinfo = soccer_containers[i].find_all('div', class_ = 'teams-info-meta-right')
        timeinfo = timeinfo[0].text.strip().split("                          \n                          -                          \n                        ")
        teaminfo = soccer_containers[i].find_all('div', class_ = 'teams-info-vert-top__live-team uppercase')
        scoresinfo = soccer_containers[i].find_all('div', class_ = "teams-info-vert-top__live-score text-center")
        hometeamscore = scoresinfo[0].text.strip()
        awayteamscore = scoresinfo[1].text.strip()
        typeleague = leagueinfo[0]
        league = leagueinfo[-1]
        hometeam = teaminfo[0].text.strip()
        awayteam = teaminfo[1].text.strip()
        # Odds
        oddsinfo = soccer_containers[i].find_all('div', class_ = "odds__container num3")

        newdict = { i+1: {'typeleague': typeleague,
                   'league': league,
                   'Session': timeinfo[0],
                   'time' :timeinfo[1],
                   'hometeam' : hometeam,
                   'awayteam': awayteam,
                   'hometeamscore': hometeamscore,
                   'awayteamscore' : awayteamscore,
    #                 'Betting': float(awayteamscore)- float(hometeamscore)
                         }}
        gamedict.update(newdict)
    return gamedict


def find02(fh, recentlysend):
    fh1 = fh[fh.hometeamscore >= 2]
    fh2 = fh1[fh1.awayteamscore == 0]
    if fh2.empty:
        return "None"
    else:
        for i in range(len(fh2)):
            # Check if recendlysend has new data
            if recentlysend.isin([fh2.iloc[i, fh2.columns.get_loc('hometeam')]]).any().any():
                print('fh2 added 02')
            else:
                message = "{} has scored {} against {} which has {}, Session is {} time is {}".format(fh2.iloc[i, fh2.columns.get_loc('hometeam')], fh2.iloc[i, fh2.columns.get_loc('hometeamscore')], fh2.iloc[i, fh2.columns.get_loc('awayteam')], fh2.iloc[i, fh2.columns.get_loc('awayteamscore')], fh2.iloc[i, fh2.columns.get_loc('Session')], fh2.iloc[i, fh2.columns.get_loc('time')])
                notifyme("Betika", message)
                # webscrapinghub.sendmessage(message, "My Messages")
        return recentlysend.append(fh2)

def find12(fh, recentlysend):
    fh1 = fh[fh.hometeamscore == 1]
    fh2 = fh1[fh1.awayteamscore == 2]
    if fh2.empty:
        return "None"
    else:
        for i in range(len(fh2)):
            if recentlysend.isin([fh2.iloc[i, fh2.columns.get_loc('hometeam')]]).any().any():
                print('fh2 added 12')
            else:
                message = "{} has scored {} against {} which has {}, Session is {} time is {}".format(fh2.iloc[i, fh2.columns.get_loc('hometeam')], fh2.iloc[i, fh2.columns.get_loc('hometeamscore')], fh2.iloc[i, fh2.columns.get_loc('awayteam')], fh2.iloc[i, fh2.columns.get_loc('awayteamscore')], fh2.iloc[i, fh2.columns.get_loc('Session')], fh2.iloc[i, fh2.columns.get_loc('time')])
                notifyme("Betika", message)
                # webscrapinghub.sendmessage(message, "My Messages")
        return recentlysend.append(fh2)

def main():
    # try:
    #     webscrapinghub.openbrowser()
    #     webscrapinghub.sendmessage("Bet responsibly!", "My Messages")
    # except:
    #     print("Internet Problem")
    newdict = { 'typeleague': [],
               'league': [],
               'Session': [],
               'time' : [],
               'hometeam' : [],
               'awayteam': [],
               'hometeamscore': [],
               'awayteamscore' : [],
#                 'Betting': float(awayteamscore)- float(hometeamscore)
                     }
    recentlysend = pd.DataFrame(newdict)
    startime = time.time()
    while True:
        url = "https://www.betika.com/lite/live?ck=1"
        try:
            res = get(url)
        except Exception as e:
            print(e)
            time.sleep(4)
        soup = BeautifulSoup(res.content,'lxml')
        soccer_containers = soup.find_all('div', class_="game highlights--item")
        gamedict = gamequery(soccer_containers)
        df = pd.DataFrame(gamedict)
        fh = df.T.replace("-", 0)
        fh['awayteamscore'] = fh.awayteamscore.astype(int)
        fh['hometeamscore'] = fh.hometeamscore.astype(int)
        df = pd.DataFrame(fh)

        recentlysend1 = find02(df, recentlysend)
        if type(recentlysend1) is str:
            recentlysend2 = find12(df, recentlysend)
        else:
            recentlysend2= find12(df, recentlysend1)
            if type(recentlysend2) is str:
                print("............")
            else:
                recentlysend = recentlysend2
                print(recentlysend)
        time.sleep(60*3)
        restartime = time.time() - startime
        # print(restartime)
        if restartime >= 7*60:
            print(restartime)
            recentlysend.to_csv('footballlogs.txt', mode='a', index = False, header=None)
            recentlysend = pd.DataFrame(newdict)
            startime = time.time()
if __name__ == "__main__":
    main()
