import pyautogui,time,math
from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_bmi2.exe'
#chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 2, 'Ponder': 'true'})
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)

pts=[[529,577,625,672,720,768,816,863],[259,307,354,402,450,498,545,593]]
table={'a':pts[0][0],'b':pts[0][1],'c':pts[0][2],'d':pts[0][3],'e':pts[0][4],'f':pts[0][5],'g':pts[0][6],'h':pts[0][7]}
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





color=''
sufix='KQkq'
past='rnbkqbnr/pppppppp/8/8/8/8/PPPPPPP/RNBKQBNR'
no=0
sflgw={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
sflgb={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
geto='-'
#for i in range(1):
while True:
    
    
    im = pyautogui.screenshot()
    
    if color=='':
        
        chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4, 'Ponder': 'true'})
        time.sleep(5)
        if tell_color_dis(im.getpixel((552,629)),(246,246,244),17.146428199482248):
            color='w'
            #sufix='KQ'
        else:
            color='b'
            #sufix='kq'
    if tell_color_dis(im.getpixel((899,73)),(10,18,4),30):#or True:
        
        print(im.getpixel((899,73)))
        time.sleep(2)
        fen=''
        for c in range(8):
            spaces=0
            if color=='b':
                    c=7-c
            for r in range(8):
                uth=0
                colors=''
                fen_part=''
                start=(529,259)
                
                blk=(pts[0][r]+23,pts[1][c]+23)
                colors=getblockcolor(im.getpixel((pts[0][r]+5,pts[1][c]+5)))
                ptschk=[(blk[0]-7,blk[1]-5),(blk[0]+7,blk[1]-5),(blk[0]+6,blk[1]+2),(blk[0]-6,blk[1]+2),#pawn
                        (blk[0]-9,blk[1]+1),(blk[0]-5,blk[1]+5),(blk[0],blk[1]-14),#knight
                        (blk[0]-8,blk[1]-5),(blk[0],blk[1]-9),(blk[0]-12,blk[1]-6),#(blk[0]-7,blk[1]-5),=pawn[0]#quine
                        (blk[0]-5,blk[1]),(blk[0]+7,blk[1]),(blk[0]-5,blk[1]+1),(blk[0]+7,blk[1]+1),#raja
                        (blk[0]-8,blk[1]-13),(blk[0]-7,blk[1]-13),(blk[0]+2,blk[1]-2),(blk[0]+2,blk[1]-1)#hathi
                        ]
                ttbl=[]
                for pt in ptschk:
                    ttbl.append(see(im.getpixel(pt),colors))
                cmn=see(im.getpixel((blk[0],blk[1]+13)),'')!=True
                if ttbl[0]and ttbl[1]and ttbl[2]and ttbl[3] and cmn:
                    uth+=1
                    fen_part='p'
                if ttbl[4]!=True and ttbl[5]and ttbl[6] and cmn:
                    uth+=1
                    fen_part='n'
                if ttbl[7] and ttbl[8] and ttbl[0]and ttbl[9]!=True and cmn:
                    uth+=1
                    fen_part='q'
                if ttbl[10]and ttbl[11]and ttbl[12]and ttbl[13]and cmn:
                    uth+=1
                    fen_part='k'
                if  (ttbl[14]!=True or ttbl[15]!=True ) and cmn and fen_part=='' :
                    uth+=1
                    fen_part='r'
                if uth ==0 and cmn:
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
                
        
        pr=fen[:len(fen)-1]+' '+color+' '+sufix+' - 0 '+str(no))#'KQkq - 0 1')
        no+=1
        print(pr)
        #'''
        chessEngine.setposition(pr)
        move = chessEngine.bestmove()
        move=move['bestmove']
        print(move,len(move))
        tem=past.split('/')
        tem2=pr.split('/')
        


        if tem[0][0]!=tem2[0][0] and 'k' in sufix:
            sufix=sufix.replace('k','')
        if tem[0][7]!=tem2[0][7] and 'q' in sufix:
            sufix=sufix.replace('q','')
        if tem[7][0]!=tem[7][0]and 'K' in sufix:
            sufix=sufix.replace('K','')
        if past[7]!=pr[7] and 'q' in sufix:
            sufix=sufix.replace('q','')


            
        if move[:2]=='a1' and 'K' in sufix:
            sufix=sufix.replace('K','')
        if move[:2]=='h1' and 'Q' in sufix:
            sufix=sufix.replace('Q','')
        if  move[:2]=='d1'  and sufix!='':
            sufix=sufix.replace('K','').replace('Q','')
        if move[:2]=='a8' and 'k' in sufix:
            sufix=sufix.replace('k','')
        if move[:2]=='h8' and 'q' in sufix:
            sufix=sufix.replace('q','')
        if  move[:2]=='d8'  and sufix!='':
            sufix=sufix.replace('k','').replace('q','')
            
        if move[:2]==move[:1]+'2'and sflgw[move[:1]]==0 and move[2:]==move[3:]+'4':
            geto=move[:1]+'3'
        else:
            geto='-'
        if move[:2]==move[:1]+'7'and sflgw[move[:1]]==0 and move[2:]==move[3:]+'5':
            geto=move[:1]+'6'
        else:
            geto='-'
        if color =='w':
            pyautogui.click(table[move[0]]+23,pts[1][7-(int(move[1])-1)]+23, button='left')
            time.sleep(1)
            pyautogui.click(table[move[2]]+23,pts[1][7-(int(move[3])-1)]+23, button='left')
            

        else:
            pyautogui.click(table[move[0]]+23,pts[1][(int(move[1])-1)]+23, button='left')
            time.sleep(1)
            pyautogui.click(table[move[2]]+23,pts[1][(int(move[3])-1)]+23, button='left')
            
        pyautogui.click(724,796, button='left')
        time.sleep(0.5)
        print('end')
        #input('next =')'''
