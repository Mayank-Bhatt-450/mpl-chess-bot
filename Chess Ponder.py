import pyautogui,time,math,os
import win32gui,win32con
from stockfishpy.stockfishpy import *
from playsound import playsound
tim1=time.time()
starttime=[tim1]
'''position fen r1b1kb1r/ppp2ppp/3p1q1n/4p3/3nP3/1PN2N2/PBPPQPPP/R3KB1R w KQkq - 0 7
go wtime 500000 btime 500000'''
STOCKFISH_PATH="C:\\Users\\bhatt\\Desktop\\stockfish-10-win (1)\\stockfish-10-win\\Windows\\stockfish_10_x64_bmi2.exe"
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)

pts=[[529,577,625,672,720,768,816,863],[259,307,354,402,450,498,545,593]]
tablew={'a':pts[0][0],'b':pts[0][1],'c':pts[0][2],'d':pts[0][3],'e':pts[0][4],'f':pts[0][5],'g':pts[0][6],'h':pts[0][7]}
tableb={'a':pts[0][7],'b':pts[0][6],'c':pts[0][5],'d':pts[0][4],'e':pts[0][3],'f':pts[0][2],'g':pts[0][1],'h':pts[0][0]}
def see(s,c):
    if c=='w':
        if(
    (tell_color_dis(s,(236,239,203),56.28498911788115 )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
    (tell_color_dis(s,(250,254,134),161.1148658566304  )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)):
            return True
        else:
            return False
    if c=='b':
        if (tell_color_dis(s,(117,155,77),59.69087032369355 )or tell_color_dis(s,(119,217,58),110.98198051936178 )):
            return True
        else:
            return False
    if c=='r':
        if tell_color_dis(s,(209,72,70),59.2452529743945  ):
            return True
        else:
            return False
    else:
        if(
(tell_color_dis(s,(236,239,203),56.28498911788115 )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
(tell_color_dis(s,(250,254,134),161.1148658566304  )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
tell_color_dis(s,(117,155,77),59.69087032369355 )or
tell_color_dis(s,(119,217,58),110.98198051936178 )):
            return True
        else:
            return False
def getblockcolor(s):
    if(
(tell_color_dis(s,(236,239,203),56.28498911788115 )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
(tell_color_dis(s,(250,254,134),161.1148658566304  )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)):
        return 'w'
    if (tell_color_dis(s,(117,155,77),59.69087032369355 )or tell_color_dis(s,(119,217,58),110.98198051936178 )):
        return 'b'
    if tell_color_dis(s,(209,72,70),59.2452529743945  ):
        return 'r'



def extend(s):
    atem1=''
    for iii in s:
        if ord(iii)>=49 and ord(iii)<=57:
                atem1+=''*int(iii)
        else:
            atem1+=iii
    return atem1
halfclock=0
hcflag=True
color=''
sufix='KQkq'
past='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
no=1
sflgw={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
sflgb={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
geto='-'
startmatch=0
for i in range(1):

#while True:
    im = pyautogui.screenshot()
    
    if color=='':
        
        chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true',
                                                    "Syzygy50MoveRule":'false'},depth=14)
        hwnd = win32gui.FindWindow(None, STOCKFISH_PATH)
        Minimize=hwnd
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        time.sleep(0.7)
        if tell_color_dis(im.getpixel((736,759)),(63,63,63),17.146428199482248):
            color='b'
            #sufix='KQ'
        else:
            color='w'
            #sufix='kq'
    
    if tell_color_dis(im.getpixel((899,73)),(10,18,4),30):#or True:
        
        print(im.getpixel((899,73)),'\n','start#########################################################')
        playsound('0.mp3') 
        time.sleep(0.3)
        im = pyautogui.screenshot()
        fen=''
        for c in range(8):
            spaces=0
            if color=='b':
                    c=7-c
            for r in range(8):
                if color=='b':
                    r=7-r
                uth=0
                colors=''
                fen_part=''
                start=(529,259)
                
                blk=(pts[0][r]+23,pts[1][c]+23)
                colors=getblockcolor(im.getpixel((pts[0][r]+5,pts[1][c]+5)))
                ptschk=[(blk[0]-7,blk[1]-5),(blk[0]+7,blk[1]-5),(blk[0]+6,blk[1]+2),(blk[0]-6,blk[1]+2),#pawn
                        (blk[0]-10,blk[1]+1),(blk[0]-7,blk[1]+6),(blk[0],blk[1]-15),#knight
                        (blk[0]-8,blk[1]-5),(blk[0],blk[1]-9),(blk[0]-12,blk[1]-6),#(blk[0]-7,blk[1]-5),=pawn[0]#quine
                        (blk[0]-5,blk[1]),(blk[0]+7,blk[1]),(blk[0]-5,blk[1]+1),(blk[0]+7,blk[1]+1),#raja
                        (blk[0]-8,blk[1]-13),(blk[0]-7,blk[1]-13),(blk[0]+2,blk[1]-2),(blk[0]+2,blk[1]-1),#hathi
                        (blk[0]+7,blk[1]-5),(blk[0]-9,blk[1]-5),(blk[0]-1,blk[1]-9),(blk[0]+8,blk[1]-5),#rani
                        ]
                ttbl=[]
                for pt in ptschk:
                    ttbl.append(see(im.getpixel(pt),colors))
                cmn=see(im.getpixel((blk[0],blk[1]+13)),'')!=True
                if ttbl[0]and ttbl[1]and ttbl[2]and ttbl[3] and cmn and fen_part=='':
                    uth+=1
                    fen_part='p'
                if ttbl[4]!=True and ttbl[5]and ttbl[6] and cmn and fen_part=='':
                    uth+=1
                    fen_part='n'
                #if(cmn and fen_part==''):
                    #print(ttbl[7] , ttbl[8] , ttbl[18],ttbl[9]!=True,c,r)
                    #print(blk,(blk[0]-8,blk[1]-5),(blk[0],blk[1]-9),(blk[0]-12,blk[1]-6),(blk[0]+7,blk[1]-5))
                if (ttbl[7]or ttbl[19]) and (ttbl[8]or ttbl[20] )and (ttbl[18]or ttbl[21])and ttbl[9]!=True and cmn and fen_part=='':
                    uth+=1
                    fen_part='q'
                    
                if ttbl[10]and ttbl[11]and ttbl[12]and ttbl[13]and cmn and fen_part=='':
                    uth+=1
                    fen_part='k'
                if  (ttbl[14]!=True or ttbl[15]!=True ) and cmn and fen_part=='' and ttbl[10]!=True and ttbl[12]!=True :
                    uth+=1
                    fen_part='r'
                if uth ==0 and cmn and fen_part=='':
                    fen_part='b'
                if fen_part=='':
                    spaces+=1 
                else:
                    if tell_color_dis(im.getpixel((blk[0],blk[1]+13)),(246,246,244),17.146428199482248):
                        fen_part=fen_part.upper()
                    if spaces!=0:
                        fen+=str(spaces)+fen_part
                        spaces=0
                    else:
                        fen+=fen_part
            if spaces!=0:
                fen+=str(spaces)+'/'
                spaces=0
            else:
                fen+='/'
        

        tem=extend(past).split('/')
        tem2=extend(fen[:len(fen)-1]).split('/')
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
        pasthalfclock=(past.count('p')+past.count('r')+past.count('n')+past.count('b')+
                   past.count('q')+past.count('k')+past.count('P')+past.count('R')+
                   past.count('N')+past.count('K')+past.count('Q'))
        fenhalfclock=(fen[:len(fen)-1].count('p')+fen[:len(fen)-1].count('r')+fen[:len(fen)-1].count('n')+fen[:len(fen)-1].count('b')+
                   fen[:len(fen)-1].count('q')+fen[:len(fen)-1].count('k')+fen[:len(fen)-1].count('P')+fen[:len(fen)-1].count('R')+
                   fen[:len(fen)-1].count('N')+fen[:len(fen)-1].count('K')+fen[:len(fen)-1].count('Q'))
        #print(pasthalfclock ,fenhalfclock)
        
        if pasthalfclock ==fenhalfclock:
            hcflag=True
        else:
            hcflag=False
        #print(hcflag)
        for item in range(8):
            if tem[item].count('p')==tem2[item].count('p') and tem[item].count('P')==tem2[item].count('P'):
                pass
            else:
                hcflag=False
        if hcflag==True:
            halfclock+=2
        else:
            halfclock=0
        pr=fen[:len(fen)-1]+' '+color+' '+sufix+' '+geto+' '+str(halfclock)+' '+str(no)#'KQkq - 0 1')
        no+=1
        print(pr)
        mp=''
        for temm in range(8):
            if color!='w':
                temm=7-temm
            mp+=tem2[temm]+'\n'
        print(mp)
        f=os.listdir('.\\data')
        k=0
        pth=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        while True:
            g=str(k)+'.png'
            if  g in f:
               k+=1
            else:
                im.save(pth+'\\chess\\data\\'+g,"PNG")
                break
        files=open(pth+'\\chess\\data\\fen.txt','a')
        files.write(g+'------'+pr+'\n')
        files.close()
        past=fen[:len(fen)-1]####
        #'''
        move=''
        if (fen[:len(fen)-1].count('p')<=8 and fen[:len(fen)-1].count('r')<= 3 and fen[:len(fen)-1].count('n')<= 3 and fen[:len(fen)-1].count('b')<=3 and
                    fen[:len(fen)-1].count('k')<=1 and fen[:len(fen)-1].count('P')<=8 and fen[:len(fen)-1].count('R')<=3 and
                   fen[:len(fen)-1].count('N')<=3 and fen[:len(fen)-1].count('K')<=1):
            chessEngine.setposition(pr)
            move = chessEngine.bestmove()
            move=move['bestmove']
            print(move)
            
                
            if color =='w' and move!='':
                pyautogui.click(tablew[move[0]]+23,pts[1][7-(int(move[1])-1)]+23, button='left')
                time.sleep(0.5)
                pyautogui.click(tablew[move[2]]+23,pts[1][7-(int(move[3])-1)]+23, button='left')
                

            elif move!='':
                pyautogui.click(tableb[move[0]]+23,pts[1][(int(move[1])-1)]+23, button='left')
                time.sleep(0.5)
                pyautogui.click(tableb[move[2]]+23,pts[1][(int(move[3])-1)]+23, button='left')
                
            pyautogui.moveTo(724,796)
            if startmatch==0:
                time.sleep(2)
                startmatch=1
            else:
                time.sleep(1)
            print('end##########################################################')
        else:
            srt=time.time()-starttime[0]
            raise Exception('\n \nGAME ENDED \n{}\n'.format(str(int(srt/60))+':'+str(round(((srt/60)-int(srt/60))*60))))
            pass
        
        

