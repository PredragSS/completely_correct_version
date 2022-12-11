from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import StaticReqConf
from Assignment import assignment

class Page:
    def __init__(self):
        self.root=Tk()
        self.root.title("Assignment Analiser MainMenu")
        self.root.resizable(False, False)
        self.root.geometry('400x250')

        self.root.configure(bg='white')

        self.root.mainloop()

    def readRequirements(self, path):
        os.chdir(path)
        c=0
        for i in os.listdir():
            if i.endswith('.txt'):
                btn=Button(self.root, width=50,height=10,command=lambda : print(i))
                btn.place(x=50,y=10+c*30)
                c+=1