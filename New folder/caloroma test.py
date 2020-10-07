from tkinter import *
master = Tk()
color='#B58863'
i=0
k=0
w004=PhotoImage(file=".\\w\\@.png")#blackq.png'
a=Label(master,highlightbackground="#0004FF",image=w004,
         highlightthickness=13,fg="#0004FF",bg=color,
         relief=FLAT,padx=1000,pady=12,bd=15)
a.grid(row=i, column=k,padx=10,pady=12)
a=Label(master,highlightbackground="#0004FF",image=w004,
         highlightthickness=13,fg="#0004FF",#bg=color,
         relief=SOLID,padx=12,pady=12,bd=15)
a.grid(row=i, column=k+1)
master.mainloop()


import ctypes

# Constants from the Windows API
STD_OUTPUT_HANDLE = -11
FOREGROUND_RED    = 0x0004 # text color contains red.

def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)

ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)
print ("Cherry on top")
print("dsfdsf")
ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
import sys
sys.stdout.write("\033[1;31m")
print ("All following prints will be red ...")
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

input()
