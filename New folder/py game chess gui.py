import pygame

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
###############################################exec("%s = %d" % ('x',12)))
pygame.init()
win = pygame.display.set_mode((592,592))
pygame.display.set_caption('lol')
run = True
r=pygame.image.load(".\\b\\r.png").convert()
n=pygame.image.load(".\\b\\n.png").convert()
p=pygame.image.load(".\\b\\p.png").convert()
b=pygame.image.load(".\\b\\b.png").convert()
q=pygame.image.load(".\\b\\q.png").convert()
kI=pygame.image.load(".\\b\\k.png").convert()
R=pygame.image.load(".\\w\\R.png").convert()
N=pygame.image.load(".\\w\\N.png").convert()
P=pygame.image.load(".\\w\\P.png").convert()
B=pygame.image.load(".\\w\\B.png").convert()
Q=pygame.image.load(".\\w\\Q.png").convert()
K=pygame.image.load(".\\w\\K.png").convert()
a=pygame.image.load(".\\w\\@.png").convert()
def bord():
     win.blit(pygame.image.load('bord.png'), (0,0))
     pygame.display.update()

def sett(fen):
    for i in range(0,8):
        for k in range(0,8):
            if fen[i][k]!='-':
                if fen[i][k]=='K':
                    pass
                    #print('in')
                #print(((k+1*74)+1,(i+1*74)+1))
                if fen[i][k]=='k':
                    win.blit(kI, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='q':
                    win.blit(q, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='p':
                    win.blit(p, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='n':
                    win.blit(n, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='b':
                    win.blit(b, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='r':
                    win.blit(r, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='K':
                    win.blit(K, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='Q':
                    win.blit(Q, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='R':
                    win.blit(R, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='N':
                    win.blit(N, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='B':
                    win.blit(B, ((i+1*74)+1,(k+1*74)+1))
                if fen[i][k]=='P':
                    win.blit(P, ((i+1*74)+1,(k+1*74)+1))
                
    #pygame.display.update()
    pygame.display.flip()
            
    
#for i in range(1):
while run:
    pygame.time.delay(100)
    win.blit(pygame.image.load('bord.png'), (0,0))
    sett('rnbqkbnr/pppppppp/--------/--------/--------/--------/PPPPPPPP/RNBQKBNR'.split('/'))
    pygame.display.update()
    #bord()
    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

pygame.quit()  # If we exit the loop this will execute and close our game
    
