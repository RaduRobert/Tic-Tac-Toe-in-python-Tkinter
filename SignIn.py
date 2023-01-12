from tkinter import *
from tkinter import ttk
import tkinter as tk
import SignUp
import MainMenu


class EntryWithPlaceholder(tk.Entry):

    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', alignment = "center", hider = ""):    
        super().__init__(master, justify = alignment, show = "")

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.hider = hider

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color


    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end') 
            self['fg'] = self.default_fg_color
            super().config(show = self.hider)

    def foc_out(self, *args):
        if not self.get():
            super().config(show = "")
            self.put_placeholder()


def showError(errorMsg, USER, PASS, errorCode):

    #Username Incorrect
    if errorCode == 1008:
        errorMsg.config(text = "Wrong Username.")
        errorMsg.place(rely = .45, relx = .5, anchor = "center")
        USER.place(rely = .35, relx = .5, anchor = "center")
        return

    #Password Incorrect
    if errorCode == 1009:
        errorMsg.config(text = "Wrong Password.")
        errorMsg.place(rely = .55, relx = .5, anchor = "center")
        USER.place(rely = .35, relx = .5, anchor = "center")
        PASS.place(rely = .45, relx = .5, anchor = "center")
        return

def ONC(root, x, username = ""):
    root.destroy()
    if x == "SignUp":
        SignUp.SignUp()
    if x == "MainMenu":
        MainMenu.MainMenu(username)
    

def submit(root, errorMsg, usrEntry, pwdEntry):
    passFaulty = False
    usr = '"' + usrEntry.get() + '"'
    pwd = '"' + pwdEntry.get() + '"'
    f = open("db.txt", "r")
    file = f.readlines()
    i = len(file)
    j = 0
    while j<i:
        if usr in file[j]:
            passFaulty = True
            if pwd in file[j+1]:
                ONC(root, "MainMenu", username = usr)
            break
        j = j+3
    f.close()
    if passFaulty:
        showError(errorMsg, usrEntry, pwdEntry, 1009)
    else:
        showError(errorMsg, usrEntry, pwdEntry, 1008)


def SignIn(boolean = False):
    
    
    root = tk.Toplevel()
    root.geometry('357x213+700+400')
    root.title("Tic Tac Toe - Sign In")
    img = PhotoImage(file = "../256x256.png")
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.resizable(False, False)

    if boolean:
        rcLabel = Label(root, text = "Registration Successful", fg = "green", font=("Times New Roman", 10))
        rcLabel.place(relx = .5, rely = 0.34, anchor = "center")
        
    errorMsg = Label(root, text = "", font=("Times New Roman", 10), fg = 'red')
    siLabel = Label(root, text = "Sign In", font=("Times New Roman", 20))
    siLabel.grid(row = 0, column = 0, pady = 2)
    siLabel.place(relx = .5, rely = 0.22, anchor="center")

    
    username = EntryWithPlaceholder(root, "username")
    password = EntryWithPlaceholder(root, "password", hider = "*")
    username.place(rely = .45, relx = .5,anchor = "center")
    password.place(rely = .55, relx = .5,anchor = "center")


    submitBtn = Button(root, text = "Submit", height = 1, width = 10, command = lambda: submit(root, errorMsg, username, password))
    submitBtn.place(rely = .7, relx = .5, anchor = "center")


    caHyperlink = Label(root, text = "Create account", font=("Times New Roman", 10), fg="blue", cursor="hand2")
    caHyperlink.place(rely = .82, relx = .5, anchor = "center")
    caHyperlink.bind("<Button-1>", lambda e: ONC(root, "SignUp"))




