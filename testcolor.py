import pyautogui,time,math
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)
def tell_color_dis1(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance)
#whiteblock#tell_color_dis(get,(235,238,202),130.3725431216251 )
#white2block#tell_color_dis(get,(250,254,134),161.1148658566304  )
#blackclock#tell_color_dis(get,(117,155,77),59.69087032369355 )
#black2clock#tell_color_dis(get,(119,217,58),110.98198051936178 )
g=None
a,b=(49,95,3),(10,18,4)
print(tell_color_dis(a,b,7.0710678118654755))
print(tell_color_dis1(a,b,7.0710678118654755))
im = pyautogui.screenshot()
im.save("screen_capture.png", "PNG")
'''
while True:
    im = pyautogui.screenshot()
    s=im.getpixel(pyautogui.position())
    p=(
    '\nwhiteblock=',tell_color_dis(s,(236,239,203),56.28498911788115 )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True,
    '  white2block=',tell_color_dis(s,(250,254,134),161.1148658566304  )and tell_color_dis(s,(246,246,244),17.146428199482248  )!=True,
    '  blackclock=',tell_color_dis(s,(117,155,77),59.69087032369355 ),
    '  black2clock=',tell_color_dis(s,(119,217,58),110.98198051936178 )
    )
    if p!=g:
        print(p)
        g=p
'''
#!/usr/bin/python
## get subprocess module 
import subprocess
 
## call date command ##
p = subprocess.Popen("G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_popcnt.exe", stdout=subprocess.PIPE, shell=True)
 
## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
## or None, if no data should be sent to the child.
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
print ("Command output : ", output)
print( "Command exit status/return code : ", p_status)
test = subprocess.Popen(["G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_popcnt.exe",""], stdout=subprocess.PIPE)
print (test.communicate()[0])
