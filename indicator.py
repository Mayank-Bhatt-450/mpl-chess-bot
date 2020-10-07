#'''
import win32gui,tkinter,time,psutil,win32con
from  tkinter import*
import tkinter as tk
import time
print('stockfish_10_x64_bmi2.exe'in(p.name() for p in psutil.process_iter()))
class indi:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('48x43+698+772')
        self.root.overrideredirect(True)
        self.root.configure(background='black')
        self.root.wm_attributes("-topmost", "true")
        self.flag=1
        self.flag2=1
        self.fm = Frame(self.root, width=497, height=281, bg='#4CFF00')
        self.fm.place(x=0,y=0)
        self.change()
        self.root.mainloop()
        
    def change(self):
        
        if ('stockfish_10_x64_bmi2.exe' in (p.name() for p in psutil.process_iter())):
            self.flag2=1
            if self.flag==1:
                
                self.flag=0
                self.fm.configure(bg='#4CFF00')
        else:
            self.flag=1
            if self.flag2==1:
                self.fm.configure(bg='#FF0000')
                self.flag2=0
        self.root.after(1000, self.change)
ro=indi()





