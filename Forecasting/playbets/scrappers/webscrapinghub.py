import time
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
def openbrowser():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com")
    print("Scan QR Code, And then Enter")
    input()
    print("Logged In")
def closebrowser():
    driver.quit()
def sendmessage(msg, contact):
    try:
        user = driver.find_element_by_xpath("//span[@title='{}']".format(contact))
        user.click()
        time.sleep(2)

        selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
        selected_contact.click()

        inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        time.sleep(2)
        input_box.send_keys(msg + Keys.ENTER)
        time.sleep(2)
        return("Success")
    except Exception:
        traceback.print_exc()
        return("error")
