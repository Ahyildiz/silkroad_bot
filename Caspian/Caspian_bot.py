#importlar - değişkenler
#region
from pyautogui import *
from tkinter import *
import os
import pyautogui
import time
import keyboard
import random
import win32api, win32con
global finish
finish = 0
global go 
go = 1
root = Tk()
root.title("PopBot")
global liste
global cardpoint

global box_type

#endregion

#main functions
#region main functions
def click(x,y):                                                                                                 # Tıklama fonksiyonu
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def img_click_in(png , x1 , y1 , x2 , y2 , c):                                                                  # Belirli bir alanda görsel arama ve bulunan sonuca tıklama fonksiyonu
    if pyautogui.locateOnScreen(png , region = (x1 , y1 , x2 , y2)  , confidence = c) != None :
       imgloc = pyautogui.locateOnScreen(png , region = (x1 , y1 , x2 , y2)  , confidence = c)
       imgpoint = pyautogui.center(imgloc)
       click(imgpoint.x , imgpoint.y)
    else:
        sleep(0.001)

def img_click(png , c):                                                                                          # Tüm ekranda belirli bir görsel arama ve bulunan sonuca tıklama fonksiyonu
    if pyautogui.locateOnScreen(png , confidence = c) != None :
       imgloc = pyautogui.locateOnScreen(png , confidence = c)
       imgpoint = pyautogui.center(imgloc)
       click(imgpoint.x , imgpoint.y)
    else:
        sleep(0.001)
#endregion


def _red():                                                                                                       
    global go
    go = 1

def _purple():
    global go
    go = 0


def _play():                                                                                                       # Ana fonksiyon
    sleep(3)
    while finish == 0:                                                                                             # Eğer para bitmediyse devam et bittiyse durdur
        if pyautogui.locateOnScreen('inventory.png' , confidence = 0.9) == None :                                  # Eğer envanter kapalıysa envanteri aç
            keyboard.press('ı')
            sleep(0.1)
            keyboard.release('ı')
            sleep(0.5)                          
        if pyautogui.locateOnScreen('page_11.png' , confidence = 0.9) != None :                                    # İlk sayfaya gir      
            page1_loc = pyautogui.locateOnScreen('page_11.png' , confidence = 0.9)
            pagepoint = pyautogui.center(page1_loc)
            click(pagepoint.x  , pagepoint.y)
            sleep (0.2)
            if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                                   # Kart var mı diye kontrol et
                if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                             # Kart yoksa diğer sayfaya geç          
                    page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)
                    pagepoint = pyautogui.center(page1_loc)
                    click(pagepoint.x + 64 , pagepoint.y)
                    sleep (0.2)
                    if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                           # Kart var mı diye kontrol et
                        if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                     # Kart yoksa diğer sayfaya geç                       
                            page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)
                            pagepoint = pyautogui.center(page1_loc)
                            click(pagepoint.x + 64 , pagepoint.y)
                            sleep (0.2)
                            if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                   # Kart var mı diye kontrol et 
                                sleep(0.5)
                                keyboard.press('ı')
                                sleep(0.1)
                                keyboard.release('ı')
                                sleep(0.5)
                                _mob_coin_npc()                                                                    # Son sayfada da kart yoksa "_mob_coin_npc" fonksiyonuna geç


        else:                                                                                                      # İlk sayfa açıksa
            if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                                   # Kart var mı diye kontrol et
                if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                                          
                    page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)
                    pagepoint = pyautogui.center(page1_loc)
                    click(pagepoint.x + 64 , pagepoint.y)
                    sleep (0.2)
                    if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                           # Kart var mı diye kontrol et
                        if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                     # Kart yoksa diğer sayfaya geç                      
                            page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)
                            pagepoint = pyautogui.center(page1_loc)
                            click(pagepoint.x + 64 , pagepoint.y)
                            sleep (0.2)
                            if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                   # Kart var mı diye kontrol et
                                sleep(0.5)
                                keyboard.press('ı')
                                sleep(0.1)
                                keyboard.release('ı')
                                sleep(0.5)
                                _mob_coin_npc()                                                                    # Son sayfada da kart yoksa "_mob_coin_npc" fonksiyonuna geç


        if pyautogui.locateOnScreen('inventory.png' , confidence = 0.9) != None :                                  # Hala envanter açıksa envanteri kapat
            keyboard.press('ı')
            sleep(0.1)
            keyboard.release('ı')
        sleep(0.3)
        _game()                                                                                                    # "_game" fonksiyonuna geç  
        _gori()                                                                                                    # "_gori" fonksiyonuna geç  (Yeşil itemleri takaslama fonksiyonu)
        _mob_coin_npc()                                                                                            # "_mob_coin_npc" fonksiyonuna geç (Kart satın alma fonksiyonu)



def _game():                                                                                                       # Oyunu oynama fonksiyonu          
    if pyautogui.locateOnScreen('card.png' , confidence = 0.9) == None :                                           # Eğer ekranda sarı kart yoksa;
        _startup_seq()                                                                                             # "_startup_seq" fonksiyonuna geç
    if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                                         
        page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)                                      
        pagepoint = pyautogui.center(page1_loc)                                                                    
        click(pagepoint.x , pagepoint.y)                                                                           
    sleep (0.1)                                                                                                     
    while pyautogui.locateOnScreen('card.png' , confidence = 0.9) != None :                                        # Ekranda kart olduğu sürece oyunu oyna
        img_click ('card.png' , 0.9)
        sleep(0.1)
        if pyautogui.locateOnScreen('game_area.png' , confidence = 0.7) != None :                                         
            page1_loc = pyautogui.locateOnScreen('game_area.png' , confidence = 0.7)                                      
            pagepoint = pyautogui.center(page1_loc)                                                                    
            pyautogui.moveTo(pyautogui.center(page1_loc).x, pyautogui.center(page1_loc).y , 0.2 )
            click(pagepoint.x , pagepoint.y)
        sleep(0.1)
        img_click ('play.png' , 0.7) 
        while pyautogui.locateOnScreen('game_area.png' , confidence = 0.7) == None :
            if pyautogui.locateOnScreen('error.png' , confidence = 0.9) != None :
                page1_loc = pyautogui.locateOnScreen('error.png' , confidence = 0.9)
                pagepoint = pyautogui.center(page1_loc)
                click(pagepoint.x , pagepoint.y)
            sleep(0.1)
    if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                                          # Kartlar bitince yan sayfaya geç
        page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)
        pagepoint = pyautogui.center(page1_loc)
        click(pagepoint.x + 64 , pagepoint.y)
    sleep (0.2)
    while pyautogui.locateOnScreen('card.png' , confidence = 0.9) != None :                                        # Ekranda kart olduğu sürece oyunu oyna
        img_click ('card.png' , 0.9)
        sleep(0.1)
        if pyautogui.locateOnScreen('game_area.png' , confidence = 0.7) != None :                                         
            page1_loc = pyautogui.locateOnScreen('game_area.png' , confidence = 0.7)                                      
            pagepoint = pyautogui.center(page1_loc)                                                                    
            pyautogui.moveTo(pyautogui.center(page1_loc).x, pyautogui.center(page1_loc).y , 0.2 )
            click(pagepoint.x , pagepoint.y)
        sleep(0.1)
        img_click ('play.png' , 0.7) 
        while pyautogui.locateOnScreen('game_area.png' , confidence = 0.7) == None :
            if pyautogui.locateOnScreen('error.png' , confidence = 0.9) != None :
                page1_loc = pyautogui.locateOnScreen('error.png' , confidence = 0.9)
                pagepoint = pyautogui.center(page1_loc)
                click(pagepoint.x , pagepoint.y)
            sleep(0.1)
    if pyautogui.locateOnScreen('page_1.png' , confidence = 0.9) != None :                                          # Kartlar bitince yan sayfaya geç
        page1_loc = pyautogui.locateOnScreen('page_1.png' , confidence = 0.9)
        pagepoint = pyautogui.center(page1_loc)
        click(pagepoint.x + 64 , pagepoint.y)
    sleep (0.2)
    while pyautogui.locateOnScreen('card.png' , confidence = 0.9) != None :                                        # Ekranda kart olduğu sürece oyunu oyna
        img_click ('card.png' , 0.9)
        sleep(0.1)
        if pyautogui.locateOnScreen('game_area.png' , confidence = 0.7) != None :                                         
            page1_loc = pyautogui.locateOnScreen('game_area.png' , confidence = 0.7)                                      
            pagepoint = pyautogui.center(page1_loc)                                                                    
            pyautogui.moveTo(pyautogui.center(page1_loc).x, pyautogui.center(page1_loc).y , 0.2 )
            click(pagepoint.x , pagepoint.y)
        sleep(0.1)
        img_click ('play.png' , 0.7) 
        while pyautogui.locateOnScreen('game_area.png' , confidence = 0.7) == None :
            if pyautogui.locateOnScreen('error.png' , confidence = 0.9) != None :
                page1_loc = pyautogui.locateOnScreen('error.png' , confidence = 0.9)
                pagepoint = pyautogui.center(page1_loc)
                click(pagepoint.x , pagepoint.y)
            sleep(0.1)
    img_click('x.png' , 0.9)
    sleep(0.2)
    img_click('x.png' , 0.9)
    sleep(0.2)

def _gori():                                                                                                       # Yeşil itemleri takaslama fonksiyonu 
    keyboard.press('v')                                                                                                 
    sleep(0.5)
    img_click('magic_pop_guide_gori.png' , 0.7)
    sleep(0.2)
    keyboard.release('v')
    sleep(0.2)
    img_click('exchange_item.png' , 0.9)
    sleep(1)
    if pyautogui.locateOnScreen('finish.png' , confidence = 0.9) != None :
        global finish
        finish = 1
    else:
        _inventory()
        keyboard.press('ı')
        sleep(0.1)
        keyboard.release('ı')
        sleep(0.5)

def _mob_coin_npc():                                                                                              # Kart satın alma fonksiyonu
    keyboard.press('v')
    sleep(0.5)
    img_click('mob_coin_npc.png' , 0.7)
    sleep(0.2)
    keyboard.release('v')
    sleep(0.2)
    img_click('mob_coin.png' , 0.9)
    sleep(0.7)
    if pyautogui.locateOnScreen('card.png' , confidence = 0.9) != None :
        page1_loc = pyautogui.locateOnScreen('card.png' , confidence = 0.8)
        cardpoint = pyautogui.center(page1_loc)
        keyboard.press('ctrl')
        while pyautogui.locateOnScreen('inventory_is_full.png' , confidence = 0.9) == None :
            for i in range (1 , 6):
                click(cardpoint.x , cardpoint.y)
                sleep(0.1)
          
            if pyautogui.locateOnScreen('not_enough_gold.png' , confidence = 0.9) != None :
                break
    keyboard.release('ctrl')
    sleep(0.3)
    img_click('x.png' , 0.9)
    sleep(0.2)
    img_click('x.png' , 0.9)
    sleep(0.2)

    

def _startup_seq():                                                                                                 # Başlangıç sekansı;
    sleep(0.2)
    keyboard.press('v')
    sleep(0.5)
    if pyautogui.locateOnScreen('magic_pop.png' , confidence = 0.8) != None :                                       # Magic pop'u bul ve tıkla
        page1_loc = pyautogui.locateOnScreen('magic_pop.png' , confidence = 0.8)
        pagepoint = pyautogui.center(page1_loc)
        click(pagepoint.x , pagepoint.y - 3)
    keyboard.release('v')
    sleep(0.5)
    img_click('join.png' , 0.9)
    sleep(0.5)
    if pyautogui.locateOnScreen('class.png' , confidence = 0.8) != None :                                           # Class seçimi
        page1_loc = pyautogui.locateOnScreen('class.png' , confidence = 0.8)
        pagepoint = pyautogui.center(page1_loc)
        click(pagepoint.x + 184 , pagepoint.y)                                                                      
        sleep(0.5)
        click(pagepoint.x + 142 , pagepoint.y + 35)                                                                 
        sleep(0.5)
    if pyautogui.locateOnScreen('type.png' , confidence = 0.8) != None :
        page1_loc = pyautogui.locateOnScreen('type.png' , confidence = 0.8)
        pagepoint = pyautogui.center(page1_loc)
        click(pagepoint.x + 184 , pagepoint.y)
        sleep(0.5)
        click(pagepoint.x + 142 , pagepoint.y + 35)                                                                 # Buradaki " pagepoint.y + 35" değeri " pagepoint.y + 50" yapılarak "CaspianBox"yerine "GodBless" seçilebilir
    img_click('start_the_game.png' , 0.9 )
    sleep(0.5)
    if go == 1:
        img_click('super_box.png' , 0.9 )                                                                           # Yukarıdaki değişikliğe bağlı olarak "red_box.png" yerine diğer seçeneklerden biri getirilmeli
    else:
        img_click('efsane_box.png' , 0.9)




def _inventory():
    while pyautogui.locateOnScreen("inventory.png" , confidence = 0.9) == None :
        keyboard.press('ı')
        sleep(0.1)
        keyboard.release('ı')
        sleep(1)
        sleep(2)
    if pyautogui.locateOnScreen("page_11.png", confidence = 0.9) != None :
        img_click("page_11.png" , 0.9)
        sleep(1)
    sort_inv()
    for page in range(1,3):
        out()
        sort_inv()
    sleep(0.1)
    img_click("empty.png" , 0.8)
def out():        
    loc = pyautogui.locateOnScreen("page_1.png" , confidence = 0.9)
    if loc != None:
        pagepoint = pyautogui.center(loc)
        pyautogui.moveTo(pagepoint.x + 64 , pagepoint.y, 0.1)
        click(pagepoint.x + 64 , pagepoint.y)
    sleep(0.2)
    coin = pyautogui.locateOnScreen("caspian_coin.png", confidence = 0.9)
    if coin != None:
        coin = pyautogui.center(coin)
        click(coin.x , coin.y)

def sort_inv():
    liste = list(pyautogui.locateAllOnScreen("caspian_coin.png", confidence = 0.8))
    while len(liste) > 1:
        liste.reverse()
        j = liste[0]
        for i in range(1,len(liste)):  
            click(pyautogui.center(liste[i]).x , pyautogui.center(liste[i]).y)
            pyautogui.moveTo(pyautogui.center(j).x , pyautogui.center(j).y, 0.15)
            click(pyautogui.center(j).x , pyautogui.center(j).y)                
        liste = list(pyautogui.locateAllOnScreen("caspian_coin.png", confidence = 0.8))


#GUI
#region

baslatbuton =Button(root , text="Kırmızı" , height=5 , width=22 , command=_red)
baslatbuton.grid(row=0 , column=0)

durdurbuton =Button(root , text="Mor" , height=5 , width=22 , command=_purple)
durdurbuton.grid(row=0 , column=1)

samarkandbuton =Button(root , text="Başlat" , height=5 , width=22 , command=_play)
samarkandbuton.grid(row=1 , column=0)

inventorybutton =Button(root , text="Envanter" , height=5 , width=22 , command=_inventory)
inventorybutton.grid(row=1 , column=1)

root.mainloop()

#endregion






