#'''
import win32gui,tkinter,time,psutil,win32con
from  tkinter import*
import tkinter as tk
import time
from playsound import playsound
print('stockfish_10_x64_bmi2.exe'in(p.name() for p in psutil.process_iter()))

while True:
    if ('stockfish_10_x64_bmi2.exe' in (p.name() for p in psutil.process_iter())):
                pass
    else:
        playsound('1.mp3')
        time.sleep(30)



