import tkinter as tk
from  tkinter import*
import random,time


from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\\Downloads\\stockfish-10-win (1)\\stockfish-10-win\\Windows\\stockfish_10_x64_bmi2.exe'
def extend(s):
    atem1=''
    for iii in s:
        if ord(iii)>=49 and ord(iii)<=57:
                atem1+='-'*int(iii)
        else:
            atem1+=iii
    return atem1

def setfen(past,pr):
    print(pr)
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
    '''
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
root=Tk()
#root.geometry('48x43+698+772')
#root.overrideredirect(True)
root.configure(background='black')
#root.wm_attributes("-topmost", "true")
bord=[]
no=1
t=[0,0]
at=[0,0]
w0041=PhotoImage(file=".\\w\\bg.png")#blackq.png
w004=PhotoImage(file=".\\w\\@.png")#blackq.png'
goti={'r':PhotoImage(file=".\\b\\r.png"),'n':PhotoImage(file=".\\b\\n.png"),
           'p':PhotoImage(file=".\\b\\p.png"),'b':PhotoImage(file=".\\b\\b.png"),
           'q':PhotoImage(file=".\\b\\q.png"),'k':PhotoImage(file=".\\b\\k.png"),
           'R':PhotoImage(file=".\\w\\R.png"),'N':PhotoImage(file=".\\w\\N.png"),
           'P':PhotoImage(file=".\\w\\P.png"),'B':PhotoImage(file=".\\w\\B.png"),
           'Q':PhotoImage(file=".\\w\\Q.png"),'K':PhotoImage(file=".\\w\\K.png"),
           '@':PhotoImage(file=".\\w\\@.png"),'@b':PhotoImage(file=".\\w\\@b.png")}
class btns:
    global movecount
    def __init__(self,ss,w004,color,i,k):
        self.ss=ss
        self.w004=w004
        self.color=color
        self.main(i,k)
    def configure(self,image):
        self.image=image
        self.b2.configure(image=self.image)
        
    def main(self,i,k):
        self.b2=Button(root,image=self.w004,bg=self.color,
                  command = lambda : movecount(self.ss))
        self.b2.grid(row=i, column=k)
        self.b2.config( height = 70, width = 70)
alph={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h'}
for i in range(8):
    g=[]
    for k in range(8):
        if (i+k)%2==0:
            color='#F0D9B5'
        else:
            color='#B58863'
        no+=1
        ss=alph[str(k)]+str(8-i)
        g.append(btns(ss,w004,color,i,k))
    bord.append(g)

root.update()
#input()
def change(fen,pr=''):
    global goti
    print(pr)
    lists=[]
    if '(None)'in pr:
        check=Label(root1,text='Check Mate',font=('Verdana', '20'))
        root.update()
        check.place(x=13,y=68)
        input()
    if pr!='':
        alpha={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
        lists=[alpha[pr[0]],8-int(pr[1]),alpha[pr[2]],8-int(pr[3])]
        print('in changer',fen)
    
    fen=fen#.split('/')
    
    for i in range(8):
        for k in range(8):
            if fen[i][k]!='-':
                bord[i][k].configure(goti[fen[i][k]])
            else:
                bord[i][k].configure(goti['@'])
            if pr!='' and i==lists[1] and k== lists[0] :
                bord[i][k].configure(goti['@b'])
    root.update()
#change('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'.split('/'),)
change('rnbqkbnr/pppppppp/--------/--------/--------/--------/PPPPPPPP/RNBQKBNR'.split('/'))
#change('rnbqkbnr/-ppppppp/p-------/--------/--------/--------/PPPPPPPP/RNBQKBNR'.split('/'))

chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)

past='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
past2=''
fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b - - 0 1'
fenp=''
sufix='KQkq'
mcount=[0,'']
no=1
def chess(fen):
    global sufix,past,no
    chessEngine.setposition(fen)
    move = chessEngine.bestmove()
    d1=extend(fen.split(' ')[0])
    f=setfen(d1,move['bestmove'])
    tem=extend(past).split('/')
    
    tem2=extend(f).split('/')
    change(tem2,move['bestmove'])
    #print(tem)
    #print(tem2)
    if tem[0][4]!=tem2[0][4]and sufix!='':
        sufix=sufix.replace('k','').replace('q','')
    if tem[7][4]!=tem2[7][4]and sufix!='':
        sufix=sufix.replace('K','').replace('Q','')        
    if tem2[0][0]!='r' and 'k' in sufix :
        sufix=sufix.replace('k','')
    if tem2[0][7]!='r' and 'q' in sufix :
        sufix=sufix.replace('q','')

    if tem2[7][0]!='R'and 'K' in sufix :
        sufix=sufix.replace('K','')
    if tem2[7][7]!='R'and 'Q' in sufix :
        sufix=sufix.replace('Q','')
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
            
    if sufix=='':
        sufix='-'
    return(f+' '+'b'+' '+sufix+' '+geto+' '+'0'+' '+str(no))
    no+=1
    past=f

def movecount(s):
    global fen,past,sufix,no,fenp
    print(s)
    if mcount[0]==0:
        mcount[1]+=s
        mcount[0]+=1
    elif (s!=mcount[1]):
        mcount[1]+=s
        if fenp!='':
            f=fenp.split(' ')[0]
            fenp=''
        #print('--',mcount[1])
        else:            
            d1=extend(fen.split(' ')[0])
            f=setfen(d1,mcount[1])
        tem=extend(past).split('/')
        tem2=extend(f).split('/')
        mcount[1]=''
        mcount[0]=0
        #change(tem2,move['bestmove'])
        #print(tem)
        #print(tem2)
        if tem[0][4]!=tem2[0][4]and sufix!='':
            sufix=sufix.replace('k','').replace('q','')
        if tem[7][4]!=tem2[7][4]and sufix!='':
            sufix=sufix.replace('K','').replace('Q','')        
        if tem2[0][0]!='r' and 'k' in sufix :
            sufix=sufix.replace('k','')
        if tem2[0][7]!='r' and 'q' in sufix :
            sufix=sufix.replace('q','')

        if tem2[7][0]!='R'and 'K' in sufix :
            sufix=sufix.replace('K','')
        if tem2[7][7]!='R'and 'Q' in sufix :
            sufix=sufix.replace('Q','')
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
                
        if sufix=='':
            sufix='-'
        past=f
        fen=chess(f+' '+'b'+' '+sufix+' '+geto+' '+'0'+' '+str(no))
        
        print(fen)
        #fen=chess(fen)
       
        #print(mcount)
    elif s==mcount[1]:
        mcount[1]=''
        mcount[0]=0
        #main()
    
def main():
    global fen
    change(fen)
    #chess(fen)
root.mainloop()
