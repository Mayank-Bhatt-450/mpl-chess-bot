#'''
import win32gui
hwnd = win32gui.FindWindow(None, 'Play Chess Online Against the Computer - Chess.com - Google Chrome')
x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
print(x0, y0, x1, y1)
w = x1 - x0
h = y1 - y0
win32gui.MoveWindow(hwnd,
                    472, 97,
                    w, h,
                    True)
'''

import pyautogui,time,math
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)#v25.495097567963924#h134.74791278531924

#474,421
pre=0
while True:
    count=0
    flag=0
    im=pyautogui.screenshot()
    for i in range(700):
        if tell_color_dis(im.getpixel((474+i,421)),(49,46,43),10 ):
            flag=0
            if count !=0:
                break
        else:
            flag=1
            count+=1
    if count!=pre:
        print(count)
        pre=count
#'''
        
