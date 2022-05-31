import os
from time import sleep
# import random
import glob
import requests
import json

import win32api, win32con
from pyautogui import *
import keyboard
import threading
import multiprocessing

class Bot():
    SortInventory = 0

    proccessList = []

    def __init__(self):
        self.media_dir = os.path.realpath("media")

    def run(self, method):
        process = multiprocessing.Process(target=self.runasync, args=(method,))
        process.start()
        self.proccessList.append(process)

        killer = threading.Thread(target=self.brokeProccess)
        killer.start()

    def runasync(self, method):
        if method == Bot.SortInventory:
            SortInventory(self)

    def brokeProccess(self):
        keyboard.wait('esc')
        for process in self.proccessList:
            process.terminate()
        print("İşlem bitirildi")

    def checkImage(self, name):
        pt = os.path.join(self.media_dir, "{}.png".format(name))
        if os.path.exists(pt):
            return pt

    def presskey(self, key):
        keyboard.press(key)
        sleep(0.1)
        keyboard.release(key)

    def get(self, method, isjson = False):
        r = requests.get('http://localhost/popbot/{}'.format(method))

        if isjson:
            return json.loads(str(r.text))

        return r.text


class SortInventory:

    def __init__(self, bot):
        self.bot = bot

    def run(self):
        if pyautogui.locateOnScreen(self.bot.checkImage("inventory") , confidence = 0.9) == None :
            sleep(1)
            self.bot.presskey('ı')


class BotCaspianBox():

    def __init__(self):
        pass