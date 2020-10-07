import pyautogui,time,math
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)#v25.495097567963924#h134.74791278531924
#whiteblock#tell_color_dis(get,(235,238,202),130.3725431216251 )
#white2block#tell_color_dis(get,(250,254,134),161.1148658566304  )
#blackclock#tell_color_dis(get,(117,155,77),59.69087032369355 )
#black2clock#tell_color_dis(get,(119,217,58),110.98198051936178 )
pts=[[529,577,625,672,720,768,816,863],[259,307,354,402,450,498,545,593]]
def see(s):
    if(
(tell_color_dis(s,(236,239,203),56.28498911788115 )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
(tell_color_dis(s,(250,254,134),161.1148658566304  )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True)or
tell_color_dis(s,(117,155,77),59.69087032369355 )or
tell_color_dis(s,(119,217,58),110.98198051936178 )):
        return True
    else:
        return False
f=[0,0]
for ii in range(1):
    im = pyautogui.screenshot()
    for c in range(8):
        for r in range(8):
            uth=0
            start=(529,259)
            blk=(pts[0][r]+23,pts[1][c]+23)
            ptschk=[(blk[0]-7,blk[1]-5),(blk[0]+7,blk[1]-5),(blk[0]+6,blk[1]+2),(blk[0]-6,blk[1]+2),#pawn
                    (blk[0]-9,blk[1]+1),(blk[0]-5,blk[1]+5),(blk[0],blk[1]-14),#knight
                    (blk[0]-8,blk[1]-5),(blk[0],blk[1]-9),(blk[0]-12,blk[1]-6),#(blk[0]-7,blk[1]-5),=pawn[0]#quine
                    (blk[0]-5,blk[1]),(blk[0]+7,blk[1]),(blk[0]-5,blk[1]+1),(blk[0]+7,blk[1]+1),
                    (blk[0]-8,blk[1]-13),(blk[0]-7,blk[1]-13)
                    ]
            #print (ptschk)
            ttbl=[]
            for pt in ptschk:
                ttbl.append(see(im.getpixel(pt)))
            
            #print(r,c,ttbl[0], ttbl[1], ttbl[2],ttbl[3] , see(im.getpixel((blk[0],blk[1]+13)))!=True,blk)
            if ttbl[0]and ttbl[1]and ttbl[2]and ttbl[3] and see(im.getpixel((blk[0],blk[1]+13)))!=True:
                #print('find a pawn',f[0],c,r)
                f[0]=f[0]+1
                uth+=1
            #print(c,r,ttbl[4]!=True , ttbl[5])
            if ttbl[4]!=True and ttbl[5]and ttbl[6] and see(im.getpixel((blk[0],blk[1]+13)))!=True:
                #print('find a knight' ,f[1],c,r)
                f[1]=f[1]+1
                uth+=1

            #print((blk[0]-8,blk[1]-5),(blk[0],blk[1]-9),(blk[0]-12,blk[1]-6))
            #print(c,r,ttbl[7] , ttbl[8] , ttbl[0], ttbl[9]!=True)
            if ttbl[7] and ttbl[8] and ttbl[0]and ttbl[9]!=True and see(im.getpixel((blk[0],blk[1]+13)))!=True:
                #print('find quine',c,r)
                uth+=1
                pass
            if ttbl[10]and ttbl[11]and ttbl[12]and ttbl[13]and see(im.getpixel((blk[0],blk[1]+13)))!=True:
                #print('king find',c,r)
                uth+=1
                pass
            #print (ttbl[15]!=True,(blk[0]-22,blk[1]-13))
            if  (ttbl[14]!=True or ttbl[15]!=True )and  ttbl[0]!=True and see(im.getpixel((blk[0],blk[1]+13)))!=True:#ttbl[10] and (ttbl[0]and ttbl[1]and ttbl[2]and ttbl[3] and ttbl[4] and ttbl[6] and ttbl[7] and ttbl[0]and ttbl[9])!=True:
                #print('hathi ',c,r,(blk[0]-22,blk[1]-13))
                uth+=1
                pass
            if uth ==0 and  see(im.getpixel((blk[0],blk[1]+13)))!=True:
                print('uth mil gya',c,r)
            
        
    
