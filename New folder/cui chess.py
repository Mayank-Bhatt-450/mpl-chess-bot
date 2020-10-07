import os
cui='''                            ┌────────────────────────────────────────────────────────┐
                            │░┌────────────────────────────────────────────────────┐ │
                            │░│ ║▓▓▓▓▓▓̅̅__̅̅▓▓▓▓▓▓̅̅__̅̅▓▓▓▓▓▓̅̅__̅̅▓▓▓▓▓▓̅̅__̅̅║ │ │
                            │8│ ║▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │7│ ║ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓║ │ │
                            │░│ ║  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓║ │ │
                            │░│ ║▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ║ │ │
                            │6│ ║▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │5│ ║ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓║ │ │
                            │░│ ║  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓║ │ │
                            │░│ ║▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ║ │ │
                            │4│ ║▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │3│ ║ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓║ │ │
                            │░│ ║  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓║ │ │
                            │░│ ║▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ║ │ │
                            │2│ ║▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │1│ ║ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓ |  | ▓▓  ▓▓║ │ │
                            │░│ ║__̅̅__▓▓▓▓▓▓__̅̅__▓▓▓▓▓▓__̅̅__▓▓▓▓▓▓__̅̅__▓▓▓▓▓▓║ │ │
                            │░└────────────────────────────────────────────────────┘ │
                            │░░░░░A░░░░░B░░░░░C░░░░░D░░░░░E░░░░░F░░░░░G░░░░░H░░░░░░░░│
                            └────────────────────────────────────────────────────────┘'''

print(cui)
#input()
from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_popcnt.exe'
#▓▒░█╔╗║═╚╝♚ ♛ ♜ ♝ ♞ ♟  ♔ ♕ ♖ ♗ ♘ ♙█s ▙ ▟ ▛ ▜

def extend(s):
    atem1=''
    for iii in s:
        if ord(iii)>=49 and ord(iii)<=57:
                atem1+=' '*int(iii)
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
    past[lists[1]][lists[0]]=' '
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
            if k==' ':
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
###############################################

def change(fen):#os.system('cls')
    print(fen)
    s='''                            ┌────────────────────────────────────────────────────────┐
                            │░┌────────────────────────────────────────────────────┐ │
                            │░│ ║▓▓▓▓▓▓̅̅__̅̅▓▓▓▓▓▓̅̅__̅̅▓▓▓▓▓▓̅̅__̅̅▓▓▓▓▓▓̅̅__̅̅║ │ │
                            │8│ ║▓▓'''+fen[0][0]+''' ▓▓ |'''+fen[0][1]+''' | ▓▓'''+fen[0][2]+''' ▓▓ |'''+fen[0][3]+''' | ▓▓'''+fen[0][4]+''' ▓▓ |'''+fen[0][5]+''' | ▓▓'''+fen[0][6]+''' ▓▓ |'''+fen[0][7]+''' | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │7│ ║ |'''+fen[1][0]+''' | ▓▓'''+fen[1][1]+''' ▓▓ |'''+fen[1][2]+''' | ▓▓'''+fen[1][3]+''' ▓▓ |'''+fen[1][4]+''' | ▓▓'''+fen[1][5]+''' ▓▓ |'''+fen[1][6]+''' | ▓▓'''+fen[1][7]+''' ▓▓║ │ │
                            │░│ ║  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓║ │ │
                            │░│ ║▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ║ │ │
                            │6│ ║▓▓'''+fen[2][0]+''' ▓▓ |'''+fen[2][1]+''' | ▓▓'''+fen[2][2]+''' ▓▓ |'''+fen[2][3]+''' | ▓▓'''+fen[2][4]+''' ▓▓ |'''+fen[2][5]+''' | ▓▓'''+fen[2][6]+''' ▓▓ |'''+fen[2][7]+''' | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │5│ ║ |'''+fen[3][0]+''' | ▓▓'''+fen[3][1]+''' ▓▓ |'''+fen[3][2]+''' | ▓▓'''+fen[3][3]+''' ▓▓ |'''+fen[3][4]+''' | ▓▓'''+fen[3][5]+''' ▓▓ |'''+fen[3][6]+''' | ▓▓'''+fen[3][7]+''' ▓▓║ │ │
                            │░│ ║  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓║ │ │
                            │░│ ║▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ║ │ │
                            │4│ ║▓▓'''+fen[4][0]+''' ▓▓ |'''+fen[4][1]+''' | ▓▓'''+fen[4][2]+''' ▓▓ |'''+fen[4][3]+''' | ▓▓'''+fen[4][4]+''' ▓▓ |'''+fen[4][5]+''' | ▓▓'''+fen[4][6]+''' ▓▓ |'''+fen[4][7]+''' | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │3│ ║ |'''+fen[5][0]+''' | ▓▓'''+fen[5][1]+''' ▓▓ |'''+fen[5][2]+''' | ▓▓'''+fen[5][3]+''' ▓▓ |'''+fen[5][4]+''' | ▓▓'''+fen[5][5]+''' ▓▓ |'''+fen[5][6]+''' | ▓▓'''+fen[5][7]+''' ▓▓║ │ │
                            │░│ ║  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓║ │ │
                            │░│ ║▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ║ │ │
                            │2│ ║▓▓'''+fen[6][0]+''' ▓▓ |'''+fen[6][1]+''' | ▓▓'''+fen[6][2]+''' ▓▓ |'''+fen[6][3]+''' | ▓▓'''+fen[6][4]+''' ▓▓ |'''+fen[6][5]+''' | ▓▓'''+fen[6][6]+''' ▓▓ |'''+fen[6][7]+''' | ║ │ │
                            │░│ ║▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ▓▓▓▓▓▓  ̅̅  ║ │ │
                            │░│ ║  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓  __  ▓▓▓▓▓▓║ │ │
                            │1│ ║ |'''+fen[7][0]+''' | ▓▓'''+fen[7][1]+''' ▓▓ |'''+fen[7][2]+''' | ▓▓'''+fen[7][3]+''' ▓▓ |'''+fen[7][4]+''' | ▓▓'''+fen[7][5]+''' ▓▓ |'''+fen[7][6]+''' | ▓▓'''+fen[7][7]+''' ▓▓║ │ │
                            │░│ ║__̅̅__▓▓▓▓▓▓__̅̅__▓▓▓▓▓▓__̅̅__▓▓▓▓▓▓__̅̅__▓▓▓▓▓▓║ │ │
                            │░└────────────────────────────────────────────────────┘ │
                            │░░░░░A░░░░░B░░░░░C░░░░░D░░░░░E░░░░░F░░░░░G░░░░░H░░░░░░░░│
                            └────────────────────────────────────────────────────────┘'''
    os.system('cls')
    print(s)
                
chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)
chessEngine2 = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)

past='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
past2=''
fenz='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
sufix='KQkq'
no=1
            
    
#for i in range(1):
while True:
    print('FEN 1=',fenz)
    chessEngine.setposition(fenz)
    move = chessEngine.bestmove()
    d1=extend(fenz.split(' ')[0])
    f=setfen(d1,move['bestmove'])
    tem=extend(past).split('/')
    change(tem)
    tem2=extend(f).split('/')
    #print(tem)
    #print(tem2)
    if tem[0][4]!=tem2[0][4]and sufix!='':
        #print('kq,')
        sufix=sufix.replace('k','').replace('q','')
    if tem[7][4]!=tem2[7][4]and sufix!='':
        #print('KQ')
        sufix=sufix.replace('K','').replace('Q','')
        
    if tem2[0][0]!='r' and 'k' in sufix :
        #print('k')
        sufix=sufix.replace('k','')
    if tem2[0][7]!='r' and 'q' in sufix :
        #print('q')
        sufix=sufix.replace('q','')
    #print(tem[7][0])
    if tem2[7][0]!='R'and 'K' in sufix :
        #print('K')
        sufix=sufix.replace('K','')
    if tem2[7][7]!='R'and 'Q' in sufix :
        #print('Q')
        sufix=sufix.replace('Q','')
    alf=['a','b','c','d','e','f','g','h']
    geto=' '
    if tem[1].count('p')+tem[3].count('p')==tem2[1].count('p')+tem2[3].count('p'):
        for ig in range(7):
            if tem[1][ig] =='p' and  tem2[1][ig]!='p':
                geto=alf[ig]+'6'

    if tem[6].count('P')+tem[4].count('P')==tem2[6].count('P')+tem2[4].count('P'):

        for ig in range(7):
            if tem[6][ig] =='P' and  tem2[6][ig]!='P':
                geto=alf[ig]+'3'
            
    if sufix=='':
        sufix=' '
    fen2=f+' '+'b'+' '+sufix+' '+geto+' '+'0'+' '+str(no)
    no+=1
    past=fenz[:len(fenz)-1]####
    print('FEN 2=',fen2)
    f2=chessEngine2.setposition(fen2)
    move = chessEngine2.bestmove()
    d2=extend(fen2.split(' ')[0])
    f2=setfen(d2,move['bestmove'])
    tem=extend(past).split('/')
    change(tem)
    tem2=extend(f2).split('/')
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

    geto=' '
    if tem[1].count('p')+tem[3].count('p')==tem2[1].count('p')+tem2[3].count('p'):
        for ig in range(7):
            if tem[1][ig] =='p' and  tem2[1][ig]!='p':
                geto=alf[ig]+'6'
    

    if tem[6].count('P')+tem[4].count('P')==tem2[6].count('P')+tem2[4].count('P'):

        for ig in range(7):
            if tem[6][ig] =='P' and  tem2[6][ig]!='P':
                geto=alf[ig]+'3'
            
    if sufix=='':
        sufix=' '
    fen=f2+' '+'w'+' '+sufix+' '+geto+' '+'0'+' '+str(no)
    no+=1
    past2=fen2[:len(fen2)-1]####

    

