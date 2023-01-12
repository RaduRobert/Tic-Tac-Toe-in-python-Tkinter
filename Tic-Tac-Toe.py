import tkinter as tk
from tkinter import ttk
from tkinter import *

def changeText(x,z):
    
    global bol
    global btnArray
    global gameState

    if bol == True:
        btnArray[x][z].config(text = "X")
        gameState.config(text = "O's turn")
        bol = False
    else:
        btnArray[x][z].config(text = "O")
        gameState.config(text = "X's turn")
        bol = True
        
    btnArray[x][z].config(state = DISABLED)
    checkEnd()

def DrawBoard(root, btnArray):
    for i in range(3):
        for j in range(3):
            btnArray[i][j] = ttk.Button(root, text = " ", command = lambda a = i, b = j: changeText(a,b))
            btnArray[i][j].grid(column=i, row=j, ipady = 23, padx = 5, pady = 5)

def DeleteBoard(btnArray):
    for i in range(3):
        for j in range(3):
            btnArray[i][j].destroy()

def replay():
    global bol
    DeleteBoard()
    DrawBoard()
    gameState.config(text = "X's turn")
    bol = True

def BlockBoard():
    global btnArray
    for i in range(3):
        for j in range(3):
            btnArray[i][j].config(state = DISABLED)

def Win():
    if bol:
        gameState.config(text = "O won")
        BlockBoard()
    else:
        gameState.config(text = "X won")
        BlockBoard()

def Draw():
    gameState.config(text = "It's a draw")

def checkEnd():
    global Game    
    #Horizontal winning condition    
    if(btnArray[0][0].cget('text') == btnArray[0][1].cget('text') and btnArray[0][1].cget('text') == btnArray[0][2].cget('text') and btnArray[0][0].cget('text') != ' '):    
        Win()    
    elif(btnArray[1][0].cget('text') == btnArray[1][1].cget('text') and btnArray[1][1].cget('text') == btnArray[1][2].cget('text') and btnArray[1][0].cget('text') != ' '):    
        Win()    
    elif(btnArray[2][0].cget('text') == btnArray[2][1].cget('text') and btnArray[2][1].cget('text') == btnArray[2][2].cget('text') and btnArray[2][0].cget('text') != ' '):                             
        Win()    
    #Vertical Winning Condition    
    elif(btnArray[0][0].cget('text') == btnArray[1][0].cget('text') and btnArray[1][0].cget('text') == btnArray[2][0].cget('text') and btnArray[0][0].cget('text') != ' '):    
        Win()    
    elif(btnArray[0][1].cget('text') == btnArray[1][1].cget('text') and btnArray[1][1].cget('text') == btnArray[2][1].cget('text') and btnArray[0][1].cget('text') != ' '):    
        Win()    
    elif(btnArray[0][2].cget('text') == btnArray[1][2].cget('text') and btnArray[1][2].cget('text') == btnArray[2][2].cget('text') and btnArray[0][2].cget('text') != ' '):    
        Win()    
    #Diagonal Winning Condition    
    elif(btnArray[0][0].cget('text') == btnArray[1][1].cget('text') and btnArray[1][1].cget('text') == btnArray[2][2].cget('text') and btnArray[1][1].cget('text') != ' '):    
        Win()    
    elif(btnArray[0][2].cget('text') == btnArray[1][1].cget('text') and btnArray[1][1].cget('text') == btnArray[2][0].cget('text') and btnArray[1][1].cget('text') != ' '):    
        Win()    
    #Match Tie or Draw Condition    
    elif(btnArray[0][0].cget('text')!=' ' and btnArray[0][1].cget('text')!=' ' and btnArray[0][2].cget('text')!=' ' and btnArray[1][0].cget('text')!=' ' and btnArray[1][1].cget('text')!=' ' and btnArray[1][2].cget('text')!=' ' and btnArray[2][0].cget('text')!=' ' and btnArray[2][1].cget('text')!=' ' and btnArray[2][2].cget('text')!=' '):    
        Draw()


def Game():
    
    root = tk.Tk()
    root.geometry('259x361+200+150')
    root.title("Tic Tac Toe")
    img = PhotoImage(file = "../256x256.png")
    root.tk.call('wm', 'iconphoto', root._w, img)
    #root.resizable(False, False)

    btnArray = [[0 for m in range(3)] for m in range(3)]
    btn_text = tk.StringVar()
    btn_text.set(" ")

    bol = True
    gameState = Label(root, text = "X's turn")
    gameState.grid(row = 4, column = 1, pady = 2, ipady = 1, ipadx = 7)

    DrawBoard(root, btnArray)

    btnReplay = ttk.Button(root, text = "Replay", command = lambda: replay())
    btnReplay.place(height = 30, width = 80, relx = .5, rely = .8, anchor = "center")

    btnQuit = ttk.Button(root, text = "Quit", command = lambda: quit())
    btnQuit.place(height = 30, width = 90, relx = .5, rely = .9, anchor = "center")

    root.mainloop()



Game()
