import tkinter as tk
import turtle
from PIL import Image, ImageTk
from turtlewheel import *
#from turtleProject_mmg import *
from tictac import *
from pattern4 import *
from operationwingit import *


class MainMenu:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.minsize(500, 700)
        self.master.wm_title("MENU")
        self.master.option_add("*Font", "helvetica")
        # start frame
        self.frame = tk.Frame(self.master, relief='raised', borderwidth=1, background="#eee8d5")
        self.frame.place(x=100, y=100,                    )
        self.button1 = tk.Button(self.frame, text = 'TurtleWheel', width = 25, command = ryan)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'TIC TAC', width = 25, command = gameboard)
        self.button2.pack()
        self.button3 = tk.Button(self.frame, text = 'ACE', width = 25, command = ace)
        self.button3.pack()
        self.button4 = tk.Button(self.frame, text = 'OWI', width = 25, command = wingit)
        self.button4.pack()
        self.button5 = tk.Button(self.frame, text = '****', width = 25, command = ryan)
        self.button5.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.text = tk.Label(self.frame, text="* * * * * * * * * * * * * \n \
Ryan * Greg * Javi, Mason and Trey \n  \
* * * * * * * * * * * * * \n  \
Cw. Coleman",font=('courier', '10'),background="#eee8d5" )
        self.text.pack()
        self.frame.pack(expand=True, fill='both')
        # display image
        load = Image.open("theturtle.jpg")
        render = ImageTk.PhotoImage(load)
        # labels can be text or images
        self.img = tk.Label(self.frame, image=render)
        self.img.image = render
        self.img.place(x=50, y=400)
        # * * * * * * * * *

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = ChoasWindow(self.newWindow)
    def close_windows(self):
        self.master.destroy()

class ChoasWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()


"""
apt install python3-pil python-pil python3-pil.imagetk python-pil.imagetk;
apt install python3-pil python-pil
apt install python3-pil.imagetk
apt install python-pil.imagetk
"""
