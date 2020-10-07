import pyautogui,time
from PIL import Image
import math
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
#123.69316876852982max distance
def dis(pt1,pt2=( 249 , 253 , 132 )):#191,7,5 
    #pt1=[112,186,237]#!108.54031509075327
    #(230,32,10)#(228, 177, 110)#[216,0,158]#[33,124,245]
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance)

img = Image.open("check.jpg")
print(img.getpixel((211,196)))
g=[]
k=0
pix=[0,0,0]
pixno=0
no=[  ]#[(153, 165, 177),(74, 83, 92),(77, 86, 95)]
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if (d not in no)and d[0]>50 :#(d[0]==d[1]==d[2])!=True and (d[0]!=0 and d[1]!=148 and d[2]!=255)and (d not in no)and d[0]>=112 and d[2]<=20:#and d[0]>=180  and d[2]<d[1] and d[1]<70 :#and(dis(d,(232,31,9))<=64.08587988004847 ):
            
            if d not in no :
                #g.append(d)
                fr=dis(d)
                pixno+=1
                pix[0]+=d[0]
                pix[1]+=d[1]
                pix[2]+=d[2]
                if k<fr and d not in no:
                    k=fr
                    print(d,',')

print('max_distance=',k,
      '\navrage_pts=','(',round(pix[0]/pixno),',',round(pix[1]/pixno),',',round(pix[2]/pixno),')')



