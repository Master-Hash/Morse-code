import sys
import time
import random
import ctypes
import os
columns, lines = os.get_terminal_size()
#os.system("cls")
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
    def __init__(self, x, y):
        self.X = x
        self.Y = y
STD_OUTPUT_HANDLE = -11
hOut = ctypes.windll.kernel32.GetStdHandle(-11)
INIT_POS=COORD(12,5)
ctypes.windll.kernel32.SetConsoleCursorPosition(hOut,INIT_POS)
print("ssssssss")

x = 'Staring'
for i in range(len(x)):
    sys.stdout.write('\r%s%s%s%s%.2f%%' % (x[:i + 1],' '*(6 - i), '■' * (i + 1), '□' * (6 - i), (i + 1) * 100 / 7))
    #sys.stdout.write('\r')
    #sys.stdout.flush()
    time.sleep(0.3)

# 我的进度条

'''
33% [============>         ] xs/xs
'''
e = "|/-\\"
full = 14
alr = 0
for i in range(1, 8):
    alr += 2 
    j = round(i*100/7)
    k = round(24/7*i) - 1
    if j <= 9:
        s = ' %d%% '%j
    elif j <= 99:
        s = '%d%% '%j
    else:
        s = '%d%%'%j
    sys.stdout.write('\r%s[%s>%s] %.2f/%.2f'%(s, '='*k, ' '*(23-k), alr, full))
    time.sleep(2)
else:
    sys.stdout.write('\r100%%[%s] done       '%('='*24))
    print()
for i in range(100):
    sys.stdout.write('\r%s'%e[random.randrange(0,3)])
