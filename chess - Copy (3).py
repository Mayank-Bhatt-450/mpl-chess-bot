import pyautogui,time,math
from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_bmi2.exe'
#chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 2, 'Ponder': 'true'})
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)#v25.495097567963924#h134.74791278531924
#whiteblock#tell_color_dis(get,(235,238,202),130.3725431216251 )
#white2block#tell_color_dis(get,(250,254,134),161.1148658566304  )
#blackclock#tell_color_dis(get,(117,155,77),59.69087032369355 )
#black2clock#tell_color_dis(get,(119,217,58),110.98198051936178 )
pts=[[529,577,625,672,720,768,816,863],[259,307,354,402,450,498,545,593]]
table={'a':pts[0][0],'b':pts[0][1],'c':pts[0][2],'d':pts[0][3],'e':pts[0][4],'f':pts[0][5],'g':pts[0][6],'h':pts[0][7]}
def see(s):
    if(
(tell_color_dis(s,(236,239,203),56.28498911788115 )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
(tell_color_dis(s,(250,254,134),161.1148658566304  )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
tell_color_dis(s,(117,155,77),59.69087032369355 )or
tell_color_dis(s,(119,217,58),110.98198051936178 )):
        return True
    else:
        return False
color=''
for ii in range(100):
    
    
    im = pyautogui.screenshot()
    
    if color=='':
        chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 2, 'Ponder': 'true'})
        time.sleep(5)
        if tell_color_dis(im.getpixel((552,629)),(246,246,244),17.146428199482248):
            color='w'
        else:
            color='b'
    if tell_color_dis(im.getpixel((614,774)),(82,156,7),104.06248123122954) or True:
        time.sleep(0.5)
        fen=''
        for c in range(8):
            spaces=0
            for r in range(8):
                uth=0
                fen_part=''
                start=(529,259)
                blk=(pts[0][r]+23,pts[1][c]+23)
                ptschk=[(blk[0]-7,blk[1]-5),(blk[0]+7,blk[1]-5),(blk[0]+6,blk[1]+2),(blk[0]-6,blk[1]+2),#pawn
                        (blk[0]-9,blk[1]+1),(blk[0]-5,blk[1]+5),(blk[0],blk[1]-14),#knight
                        (blk[0]-8,blk[1]-5),(blk[0],blk[1]-9),(blk[0]-12,blk[1]-6),#(blk[0]-7,blk[1]-5),=pawn[0]#quine
                        (blk[0]-5,blk[1]),(blk[0]+7,blk[1]),(blk[0]-5,blk[1]+1),(blk[0]+7,blk[1]+1),#raja
                        (blk[0]-8,blk[1]-13),(blk[0]-7,blk[1]-13)#hathi
                        ]
                ttbl=[]
                for pt in ptschk:
                    ttbl.append(see(im.getpixel(pt)))
                cmn=see(im.getpixel((blk[0],blk[1]+13)))!=True
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
                if  (ttbl[14]!=True or ttbl[15]!=True )and  ttbl[0]!=True and cmn:
                    uth+=1
                    fen_part='r'
                if uth ==0 and cmn:
                    fen_part='b'
                if fen_part=='':
                    spaces+=1 
                else:
                    if tell_color_dis(im.getpixel((blk[0],blk[1]+13)),(246,246,244),17.146428199482248)!=True:
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
                
                
        print(fen[:len(fen)-1]+' '+color+' '+'KQkq - 0 1')
        
        chessEngine.setposition(fen[:len(fen)-1]+' '+color+' '+'KQkq - 0 1')
        move = chessEngine.bestmove()
        move=move['bestmove']
        print(move,len(move))
        print(table[move[0]]+23,pts[1][int(move[1])-1]+23)
        print(table[move[2]]+23,pts[1][int(move[3])-1]+23)
        pyautogui.click(table[move[0]]+23,pts[1][int(move[1])-1]+23, button='left')
        time.sleep(0.3)
        pyautogui.click(table[move[2]]+23,pts[1][int(move[3])-1]+23, button='left')
        input('next =')
