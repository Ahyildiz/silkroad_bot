import os
from time import sleep
import requests
import json
import sys
import win32api, win32con
import pyautogui
import keyboard
import threading
import multiprocessing
import tkinter



class Bot():
    SortInventory = 0
    CoinBot = 1

    pop_class = None
    pop_type = None
    pop_extend = None

    proccessList = []

    def __init__(self):

        print("_init_bot çalışıyor")
        
        self.media_dir = os.path.realpath("media")


    def run(self, method, isrun = True):
        print("run.bot çalışıyor")
        process = multiprocessing.Process(target=self.runasync, args=(method, isrun,))
        process.start()
        self.proccessList.append(process)

        killer = threading.Thread(target=self.brokeProccess)
        killer.start()
        print("run.bot bitiyor")

    def runasync(self, method, isrun):
        print("runasync.bot çalışıyor")
        
        if isrun:
            self.img_click("appicon", 0.9)

        if method == Bot.SortInventory:
            SortInventory(self)
        elif method == Bot.CoinBot:
            CoinBot(self)

        if isrun:
            keyboard.release("v")
            self.presskey('esc')

    def brokeProccess(self):
        keyboard.wait('esc')
        for process in self.proccessList:
            process.terminate()
        tkinter.messagebox.showwarning(title="Uyarı", message="Bot durduruldu")

        print("İşlem bitirildi")

    def checkImage(self, name):
        pt = os.path.join(self.media_dir, "{}.png".format(name))
        if os.path.exists(pt):
            return pt

    def presskey(self, key):
        keyboard.press(key)
        sleep(0.1)
        keyboard.release(key)


    def click(self, x, y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def img_click(self, img, conf = 0.85):
        img = self.checkImage(img)
        if pyautogui.locateOnScreen(img , confidence = conf) != None :
            imgloc = pyautogui.locateOnScreen(img , confidence = conf)
            imgpoint = pyautogui.center(imgloc)
            self.click(imgpoint.x , imgpoint.y)
        else:
            sleep(0.001)

    def close_all(self):
        while True:
            clsbtn = pyautogui.locateOnScreen(self.checkImage("cancel") , confidence = 0.9)

            if clsbtn == None:
                break

            clsbtnpos = pyautogui.center(clsbtn)
            pyautogui.moveTo(clsbtnpos.x , clsbtnpos.y, 0.3)
            self.click(clsbtnpos.x , clsbtnpos.y)

            sleep(0.3)

        while True:
            clsbtn = list(pyautogui.locateAllOnScreen(self.checkImage("x") , confidence = 0.9))

            if len(clsbtn) == 0:
                break
            
            for cb in clsbtn:
                clsbtnpos = pyautogui.center(cb)
                pyautogui.moveTo(clsbtnpos.x , clsbtnpos.y, 0.3)
                self.click(clsbtnpos.x , clsbtnpos.y)

            sleep(0.3)

    def get(self, method, isjson = False):
        r = requests.get('http://localhost/popbot/{}'.format(method))

        if isjson:
            return json.loads(str(r.text))

        return r.text



class SortInventory:

    def __init__(self, bot):
        self.bot = bot

        self.run()

    def run(self):
        while pyautogui.locateOnScreen(self.bot.checkImage("inventory") , confidence = 0.9) == None :
            self.bot.presskey('ı')
            sleep(2)

        if pyautogui.locateOnScreen(self.bot.checkImage("page_11"), confidence = 0.9) != None :
            self.bot.img_click("page_11")
            sleep(1)

        movepage = False
        #page 1
        self.collectpage()

        caspian_coin = pyautogui.locateOnScreen(self.bot.checkImage("caspian_coin"), confidence = 0.8)
        if caspian_coin != None:
            movepage = True
            caspian_coin = pyautogui.center(caspian_coin)
            self.bot.click(caspian_coin.x , caspian_coin.y)
        
        self.nextPage()
        # page 2
        if movepage:
            liste = list(pyautogui.locateAllOnScreen(self.bot.checkImage("caspian_coin"), confidence = 0.8))
            if len(liste) > 1:
                pyautogui.moveTo(pyautogui.center(liste[1]).x , pyautogui.center(liste[1]).y, 0.2)
                self.bot.click(pyautogui.center(liste[1]).x , pyautogui.center(liste[1]).y)

        movepage = False

        self.collectpage()

        caspian_coin = pyautogui.locateOnScreen(self.bot.checkImage("caspian_coin"), confidence = 0.8)
        if caspian_coin != None:
            movepage = True
            caspian_coin = pyautogui.center(caspian_coin)
            self.bot.click(caspian_coin.x , caspian_coin.y)
        
        self.nextPage()
        # page 3
        if movepage:
            liste = list(pyautogui.locateAllOnScreen(self.bot.checkImage("caspian_coin"), confidence = 0.8))
            if len(liste) > 1:
                pyautogui.moveTo(pyautogui.center(liste[1]).x , pyautogui.center(liste[1]).y, 0.2)
                self.bot.click(pyautogui.center(liste[1]).x , pyautogui.center(liste[1]).y)

        self.collectpage()

        self.bot.close_all()
    
    def collectpage(self):
        broken = 5
        while True:
            pyautogui.moveTo(50 , 50, 0.2)
            liste = list(pyautogui.locateAllOnScreen(self.bot.checkImage("caspian_coin"), confidence = 0.8))
            
            broken -= 1

            if broken == 0:
                pyautogui.moveTo(50 , 50, 0.2)
                break

            if len(liste) <= 1:
                pyautogui.moveTo(50 , 50, 0.2)
                break

            while len(liste) > 1:

                j = liste[0]

                for i in range(1, len(liste)):
                    pyautogui.moveTo(pyautogui.center(liste[i]).x , pyautogui.center(liste[i]).y, 0.2)
                    self.bot.click(pyautogui.center(liste[i]).x , pyautogui.center(liste[i]).y)
                    pyautogui.moveTo(pyautogui.center(j).x , pyautogui.center(j).y, 0.2)
                    self.bot.click(pyautogui.center(j).x , pyautogui.center(j).y)
                    sleep(0.2)
                
                liste = list(pyautogui.locateAllOnScreen(self.bot.checkImage("caspian_coin"), confidence = 0.8))

    def nextPage(self):
        loc = pyautogui.locateOnScreen(self.bot.checkImage("page_1"), confidence = 0.9)
        if loc != None:
            pagepoint = pyautogui.center(loc)
            pyautogui.moveTo(pagepoint.x + 64 , pagepoint.y, 0.2)
            self.bot.click(pagepoint.x + 64 , pagepoint.y)
            pyautogui.moveTo(pagepoint.x - 50 , pagepoint.y - 50, 0.2)


class CoinBot():

    def __init__(self, bot):
        self.bot = bot

        self.bot.runasync(Bot.SortInventory, False)

        c = self.checkmegicpop()

        if c:
            self.buycoin()
        
        while True:

            self.megicPop()

            self.bot.runasync(Bot.SortInventory, False)

            self.buycoin()

    def checkmegicpop(self):
        self.bot.close_all()

        while pyautogui.locateOnScreen(self.bot.checkImage("inventory") , confidence = 0.9) == None :
            self.bot.presskey('ı')
            sleep(2)
        
        if pyautogui.locateOnScreen(self.bot.checkImage("page_11"), confidence = 0.9) != None :
            self.bot.img_click("page_11")
            sleep(1)

        for i in range(1,3):
            if pyautogui.locateOnScreen(self.bot.checkImage("card"), confidence = 0.95):
                return False
            self.nextPage()

        return True

    def megicPop(self):
        self.bot.close_all()

        keyboard.press("v")
        while True:
            sleep(0.1)


            mobcoin_npc = list(pyautogui.locateAllOnScreen(self.bot.checkImage("magic_pop_npc") , confidence = 0.9))

            if pyautogui.locateOnScreen(self.bot.checkImage("magic_pop_npc_bold") , confidence = 0.9) != None:
                mobcoin_npc.append(pyautogui.locateOnScreen(self.bot.checkImage("magic_pop_npc_bold") , confidence = 0.9))

            mobcoin_gori_npc = pyautogui.locateOnScreen(self.bot.checkImage("magic_pop_guide_gori"), confidence = 0.9)
            if mobcoin_gori_npc != None:
                mobcoin_gori_npc = pyautogui.center(mobcoin_gori_npc)
            else:
                mobcoin_gori_npc = pyautogui.locateOnScreen(self.bot.checkImage("magic_pop_guide_gori_bold"), confidence = 0.9)
                if mobcoin_gori_npc != None:
                    mobcoin_gori_npc = pyautogui.center(mobcoin_gori_npc)

            if 0 == 0:
                if pyautogui.center(mobcoin_npc[0]).y != mobcoin_gori_npc.y:
                    self.bot.click(pyautogui.center(mobcoin_npc[0]).x , pyautogui.center(mobcoin_npc[0]).y + 5)
                    break
                else:
                    self.bot.click(pyautogui.center(mobcoin_npc[1]).x , pyautogui.center(mobcoin_npc[1]).y + 5)
                    break
            
        keyboard.release("v")

        while pyautogui.locateOnScreen(self.bot.checkImage("join"), confidence = 0.95) == None:
            sleep(0.5)

        self.bot.img_click("join", 0.95)
        

        # pop class selector
        while pyautogui.locateOnScreen(self.bot.checkImage("class"), confidence = 0.95) == None:
            sleep(0.5)
        pop = pyautogui.locateOnScreen(self.bot.checkImage("class"), confidence = 0.9)
        pop = pyautogui.center(pop)
        pyautogui.moveTo(pop.x + 184 , pop.y, 0.2)
        self.bot.click(pop.x + 184, pop.y)

        while pyautogui.locateOnScreen(self.bot.checkImage(self.bot.pop_class), confidence = 0.9) == None:
            sleep(0.5)

        self.bot.img_click(self.bot.pop_class, 0.95)

        # pop type selector
        while pyautogui.locateOnScreen(self.bot.checkImage("type"), confidence = 0.95) == None:
            sleep(0.5)
        pop = pyautogui.locateOnScreen(self.bot.checkImage("type"), confidence = 0.9)
        pop = pyautogui.center(pop)
        pyautogui.moveTo(pop.x + 184 , pop.y, 0.2)
        self.bot.click(pop.x + 184, pop.y)

        while pyautogui.locateOnScreen(self.bot.checkImage(self.bot.pop_type), confidence = 0.9) == None:
            sleep(0.5)

        self.bot.img_click(self.bot.pop_type, 0.95)

        # start game
        startgame = pyautogui.locateOnScreen(self.bot.checkImage("start_the_game"), confidence = 0.9)
        startgame = pyautogui.center(startgame)
        pyautogui.moveTo(startgame.x , startgame.y, 0.2)
        self.bot.click(startgame.x, startgame.y)

        # pop ext selector
        while pyautogui.locateOnScreen(self.bot.checkImage(self.bot.pop_extend), confidence = 0.9) == None:
            sleep(0.5)

        pop_extend = pyautogui.locateOnScreen(self.bot.checkImage(self.bot.pop_extend), confidence = 0.9)
        pop_extend = pyautogui.center(pop_extend)
        pyautogui.moveTo(pop_extend.x , pop_extend.y, 0.2)
        self.bot.click(pop_extend.x , pop_extend.y)
        pyautogui.moveTo(pop_extend.x - 50, pop_extend.y - 50, 0.2)

        while pyautogui.locateOnScreen(self.bot.checkImage("pot"), confidence = 0.9) == None:
            sleep(0.5)

        gamepot = pyautogui.locateOnScreen(self.bot.checkImage("pot"), confidence = 0.9)
        gamepot = pyautogui.center(gamepot)

        playgame = pyautogui.locateOnScreen(self.bot.checkImage("play_deactive"), confidence = 0.9)
        playgame = pyautogui.center(playgame)

        page = 1
        while True:
            cards = list(pyautogui.locateAllOnScreen(self.bot.checkImage("card") , confidence = 0.9))

            if len(cards) == 0:
                page += 1
                if page == 4:
                    break
                self.nextPage()
            
            cards = list(pyautogui.locateAllOnScreen(self.bot.checkImage("card") , confidence = 0.9))
            
            for card in cards:
                # select card
                cardpos = pyautogui.center(card)
                pyautogui.moveTo(cardpos.x , cardpos.y, 0.2)
                self.bot.click(cardpos.x , cardpos.y)
                # move card
                pyautogui.moveTo(gamepot.x , gamepot.y, 0.2)
                self.bot.click(gamepot.x , gamepot.y)
                # click play
                pyautogui.moveTo(playgame.x , playgame.y, 0.2)
                self.bot.click(playgame.x , playgame.y)

                while pyautogui.locateOnScreen(self.bot.checkImage("potcomplate"), confidence = 0.9) == None:
                    sleep(0.25)
        
        self.bot.close_all()

        # Open pop guide
        keyboard.press("v")
        while pyautogui.locateOnScreen(self.bot.checkImage("magic_pop_guide_gori"), confidence = 0.9) == None:
            sleep(0.25)
        popguide = pyautogui.locateOnScreen(self.bot.checkImage("magic_pop_guide_gori"), confidence = 0.9)
        popguide = pyautogui.center(popguide)
        pyautogui.moveTo(popguide.x , popguide.y + 5, 0.2)
        self.bot.click(popguide.x , popguide.y + 5)
        keyboard.release("v")
        # click exchange
        while True:

            if pyautogui.locateOnScreen(self.bot.checkImage("exchange_item"), confidence = 0.9) == None:
                self.bot.img_click("exchange_item", 0.9)
                break

            if pyautogui.locateOnScreen(self.bot.checkImage("exchange_item_confirm"), confidence = 0.9) == None:
                self.bot.img_click("exchange_item_confirm_button", 0.9)
                sys.exit(0)

            sleep(0.5)

        sleep(2)


    
    def nextPage(self):
        loc = pyautogui.locateOnScreen(self.bot.checkImage("page_1"), confidence = 0.9)
        if loc != None:
            pagepoint = pyautogui.center(loc)
            pyautogui.moveTo(pagepoint.x + 64 , pagepoint.y, 0.2)
            self.bot.click(pagepoint.x + 64 , pagepoint.y)

        

    def buycoin(self):
        self.bot.close_all()

        keyboard.press("v")
        while True:
            sleep(.5)

            mobcoin_npc = pyautogui.locateOnScreen(self.bot.checkImage("mob_coin_npc"), confidence = 0.9)
            if mobcoin_npc != None:
                mobcoin_npc = pyautogui.center(mobcoin_npc)
                self.bot.click(mobcoin_npc.x , mobcoin_npc.y + 5)
                break

            else:
                mobcoin_npc = pyautogui.locateOnScreen(self.bot.checkImage("mob_coin_npc_bold"), confidence = 0.9)
                if mobcoin_npc != None:
                    mobcoin_npc = pyautogui.center(mobcoin_npc)
                    self.bot.click(mobcoin_npc.x , mobcoin_npc.y + 5)
                    break
        keyboard.release("v")

        while pyautogui.locateOnScreen(self.bot.checkImage("mob_coin"), confidence = 0.95) == None:
            sleep(0.5)
        
        mobcoin = pyautogui.locateOnScreen(self.bot.checkImage("mob_coin"), confidence = 0.95)
        mobcoin = pyautogui.center(mobcoin)
        
        self.bot.click(mobcoin.x , mobcoin.y )

        pyautogui.moveTo(mobcoin.x , mobcoin.y -50 , 0.2)

        while pyautogui.locateOnScreen(self.bot.checkImage("card"), confidence = 0.95) == None:
            sleep(0.5)

        card = pyautogui.locateOnScreen(self.bot.checkImage("card"), confidence = 0.95)
        card = pyautogui.center(card)

        while True:
            keyboard.press("ctrl")
            sleep(0.5)
            for i in range(1,10):
                self.bot.click(card.x, card.y)
                sleep(0.2)
            sleep(0.5)
            keyboard.release("ctrl")

            if pyautogui.locateOnScreen(self.bot.checkImage("inventory_is_full"), confidence = 0.8) or pyautogui.locateOnScreen(self.bot.checkImage("not_enough_gold"), confidence = 0.8):
                break

            sleep(0.5)

            print("1 yeni mob coin")

        
        self.bot.close_all()

        sleep(1)

