from tkinter import *
from tkinter import font, messagebox
import tkinter.ttk as ttk
import requests
import json
import sys
import time
from win32api import MessageBox
import multiprocessing
from bot import Bot

API_URL = "https://caspian.devsh.org/bot"
user_token = None

class login():

    def __init__(self):
        global fontstyle, fontstyle_small

        self.root = Tk()
        self.root.geometry("500x380")
        self.root.title("POPBot")
        self.root.iconbitmap(r"icon.ico")
        self.root.resizable(False, False)

        fontstyle = font.Font(family="Verdana", size=9, weight="bold")
        fontstyle_small = font.Font(family="Verdana", size=6)
        ttk.Style().configure('pad.TEntry', padding='5 6 5 6')
        ttk.Style().configure('pad.TButton', padding='5 6 5 6')

        # background
        bg = PhotoImage(file = "bg.png")
        Label(self.root, image = bg).place(x = 0, y = 0)

        Label(self.root, text="User Name", background="white", font=fontstyle).pack(pady=(80,0), padx=(0,120))

        self.username = ttk.Entry(self.root, style='pad.TEntry', width=30)
        self.username.pack(pady=(5,0))

        Label(self.root, text="Password", background="white", font=fontstyle).pack(pady=(15,0), padx=(0,130))
        
        self.password = ttk.Entry(self.root, style='pad.TEntry', show="*", width=30)
        self.password.pack(pady=(5,0))

        ttk.Button(self.root, text="Sign In", style='pad.TButton', width=30, command=self.checklogin).pack(pady=(15,0))

        Label(self.root, text="version: v0.1", background="white", font=fontstyle_small).place(x=425, y=5)

        self.root.mainloop()

    def checklogin(self):
        global user_token
        username = self.username.get()
        password = self.password.get()

        # check username and password
        if username and password:
            x = requests.post(API_URL + "/login", data = {"username": username, "passwd": password})

            data = json.loads(x.text)

            if data['state'] == 0:
                messagebox.showwarning(title="User State", message=data["message"])
            else:
                user_token = data["token"]

                self.root.destroy()
                botmain(username, password)

        else:
            messagebox.showerror(title="Empty Value", message="Enter username and password")

        


class botmain():

    tree = {
        "Caspian Pop": {
            "Caspian Box": [
                "Efsane Box",
                "Super Box",
            ],
            "GodBless": [
                "Yellow GodBless",
                "Red GodBless",
                "Turquaz GodBless",
                "Green GodBless",
                "Purple GodBless",
            ],
        },
    }

    def __init__(self, username, password):
        global fontstyle, fontstyle_small
        
        self.root = Tk()
        self.root.geometry("500x380")
        self.root.title("POPBot")
        self.root.iconbitmap(r"icon.ico")
        self.root.configure(background='white')
        self.root.resizable(False, False)

        ttk.Style().configure('pad.TButton', padding='5 6 5 6')

        bg = PhotoImage(file = "bg.png")
        Label(self.root, image = bg).place(x = 0, y = 0)

        Label(self.root, text="Class", background="white").place(x=25, y=15)
        Label(self.root, text="Type", background="white").place(x=25, y=40)
        Label(self.root, text="Extends", background="white").place(x=25, y=65)

        self.combobox_class = ttk.Combobox(self.root, state="readonly")
        self.combobox_class['values'] = list(self.tree.keys())
        self.combobox_class.current(0)
        self.combobox_class.place(x=90, y=15)
        self.combobox_class.bind("<<ComboboxSelected>>", self.selectClass)

        self.combobox_type = ttk.Combobox(self.root, state="readonly")
        self.combobox_type.place(x=90, y=40)
        self.combobox_type.bind("<<ComboboxSelected>>", self.selectType)

        self.combobox_ext = ttk.Combobox(self.root, state="readonly")
        self.combobox_ext.place(x=90, y=65)
        self.combobox_ext.bind("<<ComboboxSelected>>", self.selectExt)

        self.selectClass(NONE)
        self.selectType(NONE)
        self.selectExt(NONE)

        self.sort_inv = ttk.Button(self.root, text="Sort Inventory", style='pad.TButton', width=30, command=self.sortInventory)
        self.sort_inv.place(x=260, y=15)

        self.btn2 = ttk.Button(self.root, text="Coin Bot", style='pad.TButton', width=30, command=self.coinBot)
        self.btn2.place(x=260, y=60)

        #self.btn3 = ttk.Button(self.root, text="Sort Inventory", style='pad.TButton', width=30, command=self.sortInventory)
        #self.btn3.place(x=260, y=105)

        #self.btn4 = ttk.Button(self.root, text="Sort Inventory", style='pad.TButton', width=30, command=self.sortInventory)
        #self.btn4.place(x=260, y=150)

        self.update_clock()

        self.root.mainloop()

    def update_clock(self):
        global user_token
        x = requests.post(API_URL + "/checker", data = {"token": user_token})

        data = json.loads(x.text)

        if data['state'] == 0:
            sys.exit(0)

        self.root.after(15000, self.update_clock)

    def sortInventory(self):
        bot = Bot()
        bot.run(Bot.SortInventory)

    def coinBot(self):
        bot = Bot()

        bot.pop_class = "class_{}".format(str(self.combobox_class.get()).lower().replace(" ", ""))
        bot.pop_type = "type_{}".format(str(self.combobox_type.get()).lower().replace(" ", ""))
        bot.pop_extend = "ext_{}".format(str(self.combobox_ext.get()).lower().replace(" ", ""))

        bot.run(Bot.CoinBot)

    def selectClass(self, event):
        c = self.combobox_class.get()

        if self.tree[c]:
            self.combobox_type['values'] = list(self.tree[c].keys())
            self.combobox_type.current(0)

    def selectType(self, event):
        c = self.combobox_class.get()
        t = self.combobox_type.get()

        if self.tree[c]:
            self.combobox_ext['values'] = list(self.tree[c][t])
            self.combobox_ext.current(0)

    def selectExt(self, event):
        pass


if __name__ == "__main__":
    multiprocessing.freeze_support()
    login()