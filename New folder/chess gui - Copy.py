#'''
import win32gui,tkinter,time,psutil,win32con
from  tkinter import*
import tkinter as tk
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
        self.bord=[]
        no=1
        self.w0041=PhotoImage(file=".\\b\\b.png")#blackq.png
        self.w004=PhotoImage(file=".\\b\\n.png")#blackq.png'
        self.goti={'r':PhotoImage(file=".\\b\\r.png"),'n':PhotoImage(file=".\\b\\n.png"),
                   'p':PhotoImage(file=".\\b\\p.png"),'b':PhotoImage(file=".\\b\\b.png"),
                   'q':PhotoImage(file=".\\b\\q.png"),'k':PhotoImage(file=".\\b\\k.png"),
                   'R':PhotoImage(file=".\\w\\R.png"),'N':PhotoImage(file=".\\w\\N.png"),
                   'P':PhotoImage(file=".\\w\\P.png"),'B':PhotoImage(file=".\\w\\B.png"),
                   'Q':PhotoImage(file=".\\w\\Q.png"),'K':PhotoImage(file=".\\w\\K.png"),
                   '@':PhotoImage(file=".\\w\\@.png"),'K':PhotoImage(file=".\\w\\@.png")}
        for i in range(8):
            g=[]
            for k in range(8):
                if (i+k)%2==0:
                    color='#F0D9B5'
                else:
                    color='#B58863'
                no+=1
                self.b2=Button(self.root,text="",image=self.w0041,width=33,height=4,font=('Verdana', '13'),fg='#ffffff',bg=color)
                self.b2.grid(row=i, column=k)
                self.b2.config( height = 70, width = 70)
                g.append(self.b2)
            self.bord.append(g)
        self.change('rnbqkbnr/pppppppp/--------/--------/--------/--------/PPPPPPPP/RNBQKBNR')
        self.root.mainloop()
        
    def change(self,fen):
        fen=fen.split('/')
        for i in range(8):
            for k in range(8):
                if fen[i][k]!='-':
                    self.bord[i][k].configure(image=self.goti[fen[i][k]])#image=PhotoImage(file='.\\'+c+'\\'+fen[i][k]+".png"))#blackq.png)
                else:
                    self.bord[i][k].configure(image=self.goti['@'])
    def main():
        
            
            
        #self.root.after(1000, self.change)
ro=indi()





