#!/usr/bin/env python3 

import time, sys
import sys
import termios, sys, os
TERMIOS = termios

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

class Akinoriv:
    def __init__(self):
        pass

doll_aki = Akinoriv()


try:
    while True:
        viro = getkey().decode()
        #print(viro)
        if viro == ' ':
            print('hello^_^')
        
        if True:  
            continue
except KeyboardInterrupt:
    pass
