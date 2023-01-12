from tkinter import *
import tkinter as tk
from tkinter import ttk

class SignIn():

    def __init__():
        pass
    
    def SignIn():
        pass




def GetCenter(root):
    root.update_idletasks()
    

#It centers a window at the middle of the screen by default, but it can center it with the dx and dy as a reference
def center(win, dx = 0, dy = 0):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2 - (win.winfo_screenwidth() // 2 - win_width // 2 - dx)
    y = win.winfo_screenheight() // 2 - win_height // 2 - (win.winfo_screenheight() // 2 - win_height // 2 - dy)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

class Window(tk.Toplevel):
    def __init__(self, parent, size = "300x200", title = "Title", iconPath = ""):
        super().__init__(parent)

        self.geometry(size)
        self.title(title)
        img = PhotoImage(file = iconPath)
        self.tk.call('wm', 'iconphoto', self._w, img)

        ttk.Button(self, text = "Close", command = self.destroy).pack()

def FindMatch(root):

    cx = root.winfo_x() + 200
    cy = root.winfo_y() + 150

    fmx = 285
    fmy = 128
    
    neededx = cx - fmx // 2
    neededy = cy - fmy // 2
    fmWin = Window(root, size = f"{fmx}x{fmy}", title = "Finding Match", iconPath = "../256x256.png")
    center(fmWin, dx = neededx, dy = neededy)
    fmWin.grab_set()
    

def ONC(root):
    
    SignIn.SignIn()
    root.destroy()

def MainMenu(usr):


    root = tk.Toplevel()
    root.geometry('400x300')
    root.title("Tic Tac Toe - Main Menu")
    img = PhotoImage(file = "../256x256.png")
    root.tk.call('wm', 'iconphoto', root._w, img)
    

    menuLabel = Label(root, text = "Main Menu", font=("Times New Roman", 20))
    pnLabel = Label(root, text = F"( {usr} )", font=("Times New Roman", 10))
    menuLabel.place(relx = .5, rely = .25, anchor = "center")
    pnLabel.place(relx = .5, rely = .35, anchor = "center")
    

    fmBtn = ttk.Button(root, text = "Find Match", command = lambda: FindMatch(root))
    loBtn = ttk.Button(root, text = "Log Out", command = lambda: ONC(root))
    quitBtn = ttk.Button(root, text = "Quit", command = lambda: exit())
    fmBtn.place(rely = .6, relx = .5, anchor = "center", height = 30, width = 100)
    loBtn.place(rely = .7, relx = .5, anchor = "center", height = 30, width = 100)
    quitBtn.place(rely = .8, relx = .5, anchor = "center", height = 30, width = 100)
    


MainMenu("String")


