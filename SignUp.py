from tkinter import *
import tkinter as tk
import SignIn


def showError(root, errorMsg, USER, PASS, EMAIL, REPASS, errorCode):

    #Username already in the database.
    if errorCode == 1001:    
        errorMsg.config(text = "Username already taken.")
        errorMsg.place(rely = .36, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        return

    #Email already in the database.
    if errorCode == 1002:
        errorMsg.config(text = "Email already used.")
        errorMsg.place(rely = .46, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        EMAIL.place(rely = .38, relx = .5, anchor = "center")
        return

    #Username invalid(it is the same as the entry placeholder)
    if errorCode == 1003:
        errorMsg.config(text = "Invalid username.")
        errorMsg.place(rely = .36, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        return

    #Username confusing(it contains " " at the start or end of it)
    if errorCode == 1004:
        errorMsg.config(text = "Your username contains spaces at the start or end of it.")
        errorMsg.place(rely = .36, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        return

    #Email invalid(it does not contain "@" in it)
    if errorCode == 1005:
        errorMsg.config(text = "Invalid email.")
        errorMsg.place(rely = .46, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        EMAIL.place(rely = .38, relx = .5, anchor = "center")
        return

    #Password too small(less than 8 characters)
    if errorCode == 1006:
        errorMsg.config(text = "Password must contain at least 8 characters.")
        errorMsg.place(rely = .56, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        EMAIL.place(rely = .38, relx = .5, anchor = "center")
        PASS.place(rely = .48, relx = .5, anchor = "center")
        return

    #rePassword not matching
    if errorCode == 1007:
        errorMsg.config(text = "Passwords are not matching.")
        errorMsg.place(rely = .66, relx = .5, anchor = "center")
        USER.place(rely = .28, relx = .5, anchor = "center")
        EMAIL.place(rely = .38, relx = .5, anchor = "center")
        PASS.place(rely = .48, relx = .5, anchor = "center")
        REPASS.place(rely = .58, relx = .5, anchor = "center")
        return

    
def reset(username, email, password, rePassword, errorMsg):
    
    username.place(rely = .35, relx = .5,anchor = "center")
    email.place(rely = .45, relx = .5, anchor = "center")
    password.place(rely = .55, relx = .5,anchor = "center")
    rePassword.place(rely = .65, relx = .5, anchor = "center")

    errorMsg.config(text = "")
        

def submit(root, errorMsg, usrEntry, emlEntry, pwdEntry, rePwdEntry):

    reset(usrEntry, emlEntry, pwdEntry, rePwdEntry, errorMsg)

    if usrEntry.get() == "Name" or usrEntry.get() == "":
        showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1003)
        return

    if usrEntry.get()[0] == " " or usrEntry.get()[-1] == " ":
        showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1004)
        return

    if ("@" in emlEntry.get()) == False:
        showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1005)
        return

    if len(pwdEntry.get()) < 8:
        showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1006)
        return
    
    if pwdEntry.get() != rePwdEntry.get():
        showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1007)
        return
    
    usr = '"' + usrEntry.get() + '"'
    pwd = '"' + pwdEntry.get() + '"'
    eml = '"' + emlEntry.get() + '"'
    bol = True
    i = 0
    with open("db.txt", "r") as file:
        for line in file:
            if usr in line:
                showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1001)
                bol = False
                return
            if eml in line:
                showError(root, errorMsg, usrEntry, pwdEntry, emlEntry, rePwdEntry, 1002)
                bol = False
                return
    if bol:
        f = open("db.txt", "a")
        f.write(F"USERNAME: {usr} \n\tPASSWORD: {pwd} \n\tEMAIL: {eml} \n")
        f.close()
        ONC(root, True)
    
def ONC(root, boolean):

    SignIn.SignIn(boolean)
    root.destroy()


def SignUp():

    root = tk.Toplevel()
    root.geometry('357x230+700+400')
    root.title("Tic Tac Toe - Sign Up")
    img = PhotoImage(file = "../256x256.png")
    root.tk.call('wm', 'iconphoto', root._w, img)


    suLabel = Label(root, text = "Sign Up", font=("Times New Roman", 20))
    errorMsg = Label(root, text = "", font=("Times New Roman", 10), fg = 'red')
    suLabel.grid(row = 0, column = 0, pady = 2)
    suLabel.place(relx = .5, rely = 0.15, anchor="center")
    errorMsg.place(relx = .5, rely = .7, anchor = "center")


    username = SignIn.EntryWithPlaceholder(root, "Name")
    email = SignIn.EntryWithPlaceholder(root, "Email")
    password = SignIn.EntryWithPlaceholder(root, "Password", hider = "*")
    rePassword = SignIn.EntryWithPlaceholder(root, "Re-enter Password", hider = "*")
    username.place(rely = .35, relx = .5,anchor = "center")
    email.place(rely = .45, relx = .5, anchor = "center")
    password.place(rely = .55, relx = .5,anchor = "center")
    rePassword.place(rely = .65, relx = .5, anchor = "center")


    submitBtn = Button(root, text = "Submit",width = 10, bg ="light grey", command = lambda: submit(root, errorMsg, username, email, password, rePassword))
    submitBtn.place(rely = .78, relx = .5, anchor = "center")


    siHyperlink = Label(root, text = "Already have an acoount? Sign In.", font =("Times New Roman", 10), fg = "blue", cursor = "hand2")
    siHyperlink.place(rely = .9, relx = .5, anchor = "center")
    siHyperlink.bind("<Button-1>", lambda e: ONC(root, False))
   
