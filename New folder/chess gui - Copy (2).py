#'''
import win32gui,tkinter,time,psutil,win32con
from  tkinter import*
import tkinter as tk
from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_popcnt.exe'

print('stockfish_10_x64_bmi2.exe'in(p.name() for p in psutil.process_iter()))
def extend(s):
    atem1=''
    for iii in s:
        if ord(iii)>=49 and ord(iii)<=57:
                atem1+='-'*int(iii)
        else:
            atem1+=iii
    return atem1

def setfen(past,pr):
    alpha={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    past=past.split('/')
    for i in range(8):
        past[i]=list(past[i])
    lists=[alpha[pr[0]],8-int(pr[1]),alpha[pr[2]],8-int(pr[3])]
    try:
        s=pr[4]
    except:
        s=''
    tem=past[lists[1]][lists[0]]
    past[lists[1]][lists[0]]='-'
    if s!='':
        past[lists[3]][lists[2]]=s
    else:
        past[lists[3]][lists[2]]=tem
    #'''
    for kt in past:
        print(kt)
    #'''
    g=''
    for i in past:
        count=0
        for k in i:
            if k=='-':
               count+=1
            else:
                if count!=0:
                    g+=str(count)+k
                    count=0
                else:
                    g+=k
        if count!=0:
            g+=str(count)
        g+='/'
    return(g[:len(g)-1])
class indi:
    def __init__(self):
        self.root=Tk()
        #self.root.geometry('48x43+698+772')
        #self.root.overrideredirect(True)
        self.root.configure(background='black')
        #self.root.wm_attributes("-topmost", "true")
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
                   '@':PhotoImage(file=".\\w\\@.png")}
        
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
        #self.change('rnbqkbnr/pppppppp/--------/--------/--------/--------/PPPPPPPP/RNBQKBNR')
        self.main()
        self.root.mainloop()
        
    def change(self,fen):
        fen=fen#.split('/')
        print(fen)
        for i in range(8):
            for k in range(8):
                if fen[i][k]!='-':
                    if fen[i][k]=='K':
                        print('in')
                    self.bord[i][k].configure(image=self.goti[fen[i][k]])#image=PhotoImage(file='.\\'+c+'\\'+fen[i][k]+".png"))#blackq.png)
                else:
                    self.bord[i][k].configure(image=self.goti['@'])
        print('try to change')
        self.root.update()

    def main(self):
        self.chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)
        self.chessEngine2 = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true'},depth=14)
        self.past='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        self.past2=''
        self.fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.sufix='KQkq'
        self.no=1
        while True:
            print('self.fen 1=',self.fen)
            self.chessEngine.setposition(self.fen)
            move = self.chessEngine.bestmove()
            d1=extend(self.fen.split(' ')[0])
            f=setfen(d1,move['bestmove'])
            tem=extend(self.past).split('/')
            tem2=extend(f).split('/')
            #print(tem)
            #print(tem2)
            if tem[0][4]!=tem2[0][4]and self.sufix!='':
                #print('kq,')
                self.sufix=self.sufix.replace('k','').replace('q','')
            if tem[7][4]!=tem2[7][4]and self.sufix!='':
                #print('KQ')
                self.sufix=self.sufix.replace('K','').replace('Q','')
                
            if tem2[0][0]!='r' and 'k' in self.sufix :
                #print('k')
                self.sufix=self.sufix.replace('k','')
            if tem2[0][7]!='r' and 'q' in self.sufix :
                #print('q')
                self.sufix=self.sufix.replace('q','')
            #print(tem[7][0])
            if tem2[7][0]!='R'and 'K' in self.sufix :
                #print('K')
                self.sufix=self.sufix.replace('K','')
            if tem2[7][7]!='R'and 'Q' in self.sufix :
                #print('Q')
                self.sufix=self.sufix.replace('Q','')
            alf=['a','b','c','d','e','f','g','h']
            geto='-'
            if tem[1].count('p')+tem[3].count('p')==tem2[1].count('p')+tem2[3].count('p'):
                for ig in range(7):
                    if tem[1][ig] =='p' and  tem2[1][ig]!='p':
                        geto=alf[ig]+'6'

            if tem[6].count('P')+tem[4].count('P')==tem2[6].count('P')+tem2[4].count('P'):

                for ig in range(7):
                    if tem[6][ig] =='P' and  tem2[6][ig]!='P':
                        geto=alf[ig]+'3'
                    
            if self.sufix=='':
                self.sufix='-'
            self.fen2=f+' '+'b'+' '+self.sufix+' '+geto+' '+'0'+' '+str(self.no)
            self.change(tem)
            self.no+=1
            time.sleep(10)
            print('FEN 2=',self.fen2)
            f2=self.chessEngine2.setposition(self.fen2)
            move = self.chessEngine2.bestmove()
            d2=extend(self.fen2.split(' ')[0])
            f2=setfen(d2,move['bestmove'])
            tem=extend(self.past).split('/')
            tem2=extend(f2).split('/')
            #print(tem)
            #print(tem2)
            if tem[0][4]!=tem2[0][4]and self.sufix!='':
                self.sufix= self.sufix.replace('k','').replace('q','')
            if tem[7][4]!=tem2[7][4]and self.sufix!='':
                self.sufix= self.sufix.replace('K','').replace('Q','')      
            if tem2[0][0]!='r' and 'k' in self.sufix :
                self.sufix= self.sufix.replace('k','')
            if tem2[0][7]!='r' and 'q' in self.sufix :
                self.sufix= self.sufix.replace('q','')
            if tem2[7][0]!='R'and 'K' in self.sufix :
                self.sufix= self.sufix.replace('K','')
            if tem2[7][7]!='R'and 'Q' in self.sufix :
                self.sufix= self.sufix.replace('Q','')
            alf=['a','b','c','d','e','f','g','h']

            geto='-'
            if tem[1].count('p')+tem[3].count('p')==tem2[1].count('p')+tem2[3].count('p'):
                for ig in range(7):
                    if tem[1][ig] =='p' and  tem2[1][ig]!='p':
                        geto=alf[ig]+'6'
            

            if tem[6].count('P')+tem[4].count('P')==tem2[6].count('P')+tem2[4].count('P'):

                for ig in range(7):
                    if tem[6][ig] =='P' and  tem2[6][ig]!='P':
                        geto=alf[ig]+'3'
                    
            if self.sufix=='':
                self.sufix='-'
            self.fen=f2+' '+'w'+' '+self.sufix+' '+geto+' '+'0'+' '+str(self.no)
            self.change(tem)
            self.no+=1
            #self.root.update()

                                                  
                    
            
        #self.root.after(1000, self.change)
ro=indi()





