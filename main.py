import platform
from win32api import keybd_event
from win32con import WM_KEYDOWN, WM_KEYUP, KEYEVENTF_KEYUP # 256, 257, 2
from typing import NoReturn
import time, os, sys, warnings
import getpass

# 本程序针对 Windows 设计，Linux 在控制台及库的命令有所不同。
if not platform.system() == "Windows":
    warnings.warn("It seems you are not using Windows. You may meet with variety of bugs. ")
else:
    import winsound

# 关于识别是否处于 idle 的滑稽写法
def dec() -> bool:
    from sys import stdin
    return 'idlelib' in str(type(stdin))

if dec():
    warnings.warn("It seems you are using idle. Progress bar will not show correctly. ")

# 无验证初始化
# 暂时不能编码中文（我爱你除外）
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',



        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        ' ': ' ',      '.': '.-.-.-', '$': '...-..-',
        ':': '---...', ',': '--..--', ';': '-.-.-.',
        '?': '..--..', '=': '-...-',  "'": '.----.',
        '/': '-..-.',  '!': '-.-.--', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...',   '@': '.--.-.',

        'AR': '.-.-.', 'AS': '.--..', 'SK': '...-.-',
        #'K': '-',      
        #'BT': '-...-',
        
        'à': '.--.-',

        '我': '--...-....-...-', '爱': '---..-...--...-',
        '你': '-..----.--.....', '玩': '---..---.-.-..-',
        '笑': '----.--...-...-', '而': '-...........--..',
        '已': '-.---.-----..-.',
        }

EDOC= {} # EDOC 没有小写字母
for i in CODE:
    EDOC[CODE[i]] = i

for i in range(65, 65+26):
    CODE[chr(i+32)] = CODE[chr(i)] # 小写字母

def encode(a: str) -> str:
    ans: str = ''
    for i in a:
        ans += CODE[i]
        ans += '/'
    ans = ans.replace('/ /', ' ')
    return ans.rstrip('/ ')

def decode(a: str) -> str:
    ans = ''
    Xecades = a.split()
    for Max in Xecades:
        Mivik = Max.split('/')
        for i in Mivik:
            ans += EDOC[i]
        ans += ' '
    return ans.rstrip(' ')

def counting(encoded: str) -> int or float:
    tmp = encoded[1:] + '^'
    ans: int = 0
    def sleeping() -> int or float:
        Fuck = t if j == '.' or j == '-' else\
            3*t if j == '/' else\
            7*t if j == ' ' else 0
        return Fuck
    for i, j in zip(encoded, tmp):
        if i == '.':
            ans += t + sleeping()
        elif i == '-':
            ans += 3*t + sleeping()
    return ans

t: float = 0.3
"""
计数思路：先计算理论总时间（expected）
         记录开始时间（start = time.time()）
         不需要管 real, predicted
         unreal = 0
         length = 0
         percent = 0

         每次更新时间(beep, sleep)的时候
         real = time.time() - start
         unreal += ...
         percent = round(unreal/expected*100)
         s 是长度为 4 的 percent 生成的字符串
         length = round(unreal/expected*width)
         predicted = real*expected/unreal
         画进度条：
 0% [>                                                           ] 0.00/'%.2f'%expected
100%[============================================================] real done.
print()
(emerge 的旋转风格在进度条.py 里面)
"""
# 会 multiprocessing 的大神欢迎指教
def shine(encoded: str, width: int=60) -> NoReturn:
    def opening() -> NoReturn:
        keybd_event(20, 0, 257, 0)
        keybd_event(20, 0, 2, 0)
    def closing() -> NoReturn:
        keybd_event(20, 0, 256, 0)
        keybd_event(20, 0, 2, 0)
    def sleeping() -> NoReturn:
        time.sleep(t) if j == '.' or j == '-' else\
            time.sleep(3*t) if j == '/' else\
            time.sleep(7*t) if j == ' ' else\
            print(end='') if j == '^' else\
            warnings.warn(j)
    def countsleep() -> float:
        return t if j == '.' or j == '-' else\
            3*t if j == '/' else\
            7*t if j == ' ' else 0
    def progress_bar(width=width) -> NoReturn:
        percent = round(unreal/expected*100)
        s = ' %d%% '%percent if percent <= 9 else\
            '%d%% '%percent if percent <= 99 else\
            '%d%%'%percent
        length = round(unreal/expected*width)
        predicted = real*expected/unreal
        sys.stdout.write("\r%s[%s>%s] %.2f/%.2f      "%(s, '='*(length, width - 1)[length == width], ' '*(width - 1 - length), real, predicted))
    # init
    expected = counting(encoded)
    start = time.time()
    unreal, length, percent = 0, 0, 0
    tmp = encoded[1:] + '^'
    # init progress bar
    sys.stdout.write("\r 0%% [>%s] 0/%.2f"%(' '*(width-1), expected))
    for i, j in zip(encoded, tmp):
        if i == '.':
            opening(); winsound.Beep(440, round(t*1000))
            unreal += t; real = time.time() - start
            progress_bar()
            closing(); sleeping()
            unreal += countsleep(); real = time.time() - start
            progress_bar()
        elif i == '-':
            opening(); winsound.Beep(440, round(t*3000))
            unreal += 3*t; real = time.time() - start
            progress_bar()
            closing(); sleeping()
            unreal += countsleep(); real = time.time() - start
            progress_bar()
    sys.stdout.write("\r100%%[%s] %.2f done.       "%('='*width, real))
    print()

if __name__ == "__main__":
    for i in range(2):
        while not (testword2 := getpass.getpass("Enter what you want to say out~: ")): ...
        shine(encode(testword2))
    #shine(encode("Fuck! "), width=30)
