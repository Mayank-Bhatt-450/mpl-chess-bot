#'''
import win32gui,tkinter,time,psutil,win32con
from  tkinter import*
import tkinter as tk
import time
print('stockfish_10_x64_bmi2.exe'in(p.name() for p in psutil.process_iter()))
class indi:
    def __init__(self):
        self.root=Tk()
        #self.root.geometry('48x43+698+772')
        #self.root.overrideredirect(True)
        self.root.configure(background='black')
        self.root.wm_attributes("-topmost", "true")
        self.flag=1
        self.flag2=1
        bord=[]
        for i in range(8):
            g=[]
            for k in range(8):
                w0041=PhotoImage(file="w0041.gif")
                self.b2=Button(self.root,text="",image= w0041,width=33,height=4,font=('Verdana', '13'))#,fg='#ffffff',bg="light blue",bd=0)
                self.b2.grid(row=i, column=k)
                self.b2.config( height = 3, width = 6)
                g.append(self.b2)
            bord.append(g)
        self.change()
        self.root.mainloop()
        
    def change(self):
        self.root.after(1000, self.change)
ro=indi()





