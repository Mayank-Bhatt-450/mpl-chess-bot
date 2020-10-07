import pygame
from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_popcnt.exe'
#▓▒░█╔╗║═╚╝♚ ♛ ♜ ♝ ♞ ♟  ♔ ♕ ♖ ♗ ♘ ♙█s ▙ ▟ ▛ ▜

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
###############################################
pygame.init()
win = pygame.display.set_mode((592,592))
pygame.display.set_caption('lol')
run = True
goti={'r':pygame.image.load(".\\b\\r.png"),'n':pygame.image.load(".\\b\\n.png"),
                   'p':pygame.image.load(".\\b\\p.png"),'b':pygame.image.load(".\\b\\b.png"),
                   'q':pygame.image.load(".\\b\\q.png"),'k':pygame.image.load(".\\b\\k.png"),
                   'R':pygame.image.load(".\\w\\R.png"),'N':pygame.image.load(".\\w\\N.png"),
                   'P':pygame.image.load(".\\w\\P.png"),'B':pygame.image.load(".\\w\\B.png"),
                   'Q':pygame.image.load(".\\w\\Q.png"),'K':pygame.image.load(".\\w\\K.png"),
                   '@':pygame.image.load(".\\w\\@.png")}
def bord():
     win.blit(pygame.image.load('bord.png'), (0,0))
     pygame.display.update()

def change(fen):
    for i in range(0,8):
        for k in range(0,8):
            if fen[i][k]!='-':
                if fen[i][k]=='K':
                    pass
                    #print('in')
                #print(((k+1*74)+1,(i+1*74)+1))
                win.blit(goti[fen[i][k]], (  ((k)*74)+1,((i)*74)+1   )   )
            else:
                win.blit(goti['@'], (  ((k)*74)+1,((i)*74)+1   )   )
    pygame.display.update()
    print('should change')
                
chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)
chessEngine2 = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)

past='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
past2=''
fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
sufix='KQkq'
no=1
            
    
#for i in range(1):
while run:
    #pygame.time.delay(100)
    win.blit(pygame.image.load('bord.png'), (0,0))
    #sett('rnbqkbnr/pppppppp/--------/--------/--------/--------/PPPPPPPP/RNBQKBNR'.split('/'))
    #pygame.display.update()
    #bord()
    #change(extend('rnbqkbnr/ppp2ppp/4p3/3P4/8/5N2/PPPP1PPP/RNBQKB1R').split('/'))
    #input()
    print('FEN 1=',fen)
    chessEngine.setposition(fen)
    move = chessEngine.bestmove()
    d1=extend(fen.split(' ')[0])
    f=setfen(d1,move['bestmove'])
    tem=extend(past).split('/')
    
    tem2=extend(f).split('/')
    change(tem2)
    pygame.display.update()
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
    fen2=f+' '+'b'+' '+sufix+' '+geto+' '+'0'+' '+str(no)
    no+=1
    past=f
    print('FEN 2=',fen2)
    f2=chessEngine2.setposition(fen2)
    move = chessEngine2.bestmove()
    d2=extend(fen2.split(' ')[0])
    f2=setfen(d2,move['bestmove'])
    tem=extend(past).split('/')
    tem2=extend(f2).split('/')
    change(tem2)
    pygame.display.update()
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
    fen=f2+' '+'w'+' '+sufix+' '+geto+' '+'0'+' '+str(no)
    no+=1
    past2=f2

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

pygame.quit()  # If we exit the loop this will execute and close our game
    
