import platform
from win32api import keybd_event
from win32con import WM_KEYDOWN, WM_KEYUP, KEYEVENTF_KEYUP # 256, 257, 2
from typing import NoReturn
import time, os, sys, warnings

# 本程序针对 Windows 设计，Linux 在控制台及库的命令有所不同。
if not platform.system() == "Windows":
    warnings.warn("It seems you are not using Windows. You may meet with variety of bugs. ")
else:
    import winsound

# 验证初始化
if __name__ == "__main__":
    keybd_event(20,0,257,0) # 打开 Caps Lock
    keybd_event(20,0,2,0) # 松开 Caps Lock
    time.sleep(1)
    keybd_event(20,0,256,0) # 关闭 Caps Lock
    keybd_event(20,0,2,0) # 松开 Caps Lock

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

# 关于识别是否处于 idle 的滑稽写法
def dec() -> bool:
    from sys import stdin
    return 'idlelib' in str(type(stdin))

def encode(a: str='Hello, World! ') -> str:
    ans: str = ''
    for i in a:
        ans += CODE[i]
        ans += '/'
    ans = ans.replace('/ /', ' ')
    #ans = ans.rstrip(' ')
    return ans.rstrip('/ ')

# 解码一律大写；中文之间会出现蛋疼的空格
def decode(a: str='...././.-../.-../---/--..-- .--/---/.-./.-../-../-.-.--') -> str:
    ans = ''
    Xecades = a.split()
    for Max in Xecades:
        Mivik = Max.split('/')
        for i in Mivik:
            ans += EDOC[i]
        ans += ' '
    return ans.rstrip(' ')

'''
../.-../---/...-/./-.--/---/..-
滴=1t，嗒=3t，滴嗒间=1t，字符间(/)=3t，单词间( )=7t。
'''

t: float = 0.3
def shine(encoded: str='../.-../---/...-/./-.--/---/..-') -> NoReturn:
    cnt: float = 0
    tmp: str = encoded[1:] + '^'
    def opening() -> NoReturn:
        keybd_event(20, 0, 257, 0)
        keybd_event(20, 0, 2, 0)
    def closing() -> NoReturn:
        keybd_event(20, 0, 256, 0)
        keybd_event(20, 0, 2, 0)
    def beeping() -> NoReturn:
        x: int = round(t * 1000) if i == '.' else round(t * 3000) if i == '-' else 0
        winsound.Beep(440, x)
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
    for i, j in zip(encoded, tmp):
        if i == '.':
            opening()
            #time.sleep(t)
            winsound.Beep(440, round(t*1000))
            cnt += t
            closing()
            sleeping()
            cnt += countsleep()
        elif i == '-':
            opening()
            #time.sleep(3*t)
            winsound.Beep(440, round(t*3000))
            cnt += 3*t
            closing()
            sleeping()
            cnt += countsleep()

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

if __name__ == "__main__":
    # 获取控制台宽度
    if dec():
        warnings.warn("It seems you are in idle. ")
    else:
        # https://blog.csdn.net/countofdane/article/details/82315244 关于 Beep 的写法
        columns, lines = os.get_terminal_size()
        print("#"*columns)

    print("Fuck! ")
    print(encode())
    print(decode())
    #down = 3
    #os.system("cls")
    print(testword := encode("SOS"))
    #while down:
        #time.sleep(1)
        #print(down)
        #down -= 1
    #de = counting(testword)
    #start = time.time()
    #shine(testword)
    #ed = time.time() - start
    #print(ed, de)

#################################################################################################################
# 关于进度条
# 计时使用实际时间（所以，我的 countsleep 相当于白写）
# 在每个 cnt 变化的时候添加（是不是太蠢了）
# 用 getter 和 setter 实现监听
# 所以，时间是一个属性
class new:
    def __init__(self, testword):
        self.expected: float = counting(testword)
        self.unreal = 0
        self.start = time.time()
        self.cnt = 0
        self.word: str = testword
    @property
    def cnt(self):
        return __cnt
    @cnt.setter
    def cnt(self, value):
        # 刷新
        used = time.time() - self.start
        percent = round(self.unreal/self.expected*100)
        if self.unreal == 0:
            self.new = self.expected
        else:
            self.new = used/self.unreal*self.expected
        length = round(self.unreal/self.expected*120) - 1
        s = ' %d%% '%percent if percent <= 9 else\
            '%d%% '%percent if percent <= 99 else\
            '%d%%'%percent
        sys.stdout.write('\r%s[%s>%s] %.2f/%.2f'%(s, '='*length, ' '*(119-length), used, self.new))
        self.__cnt  = used
        
    def shine(self, encoded: str='../.-../---/...-/./-.--/---/..-') -> NoReturn:
        cnt: float = 0
        tmp: str = encoded[1:] + '^'
        def opening() -> NoReturn:
            keybd_event(20, 0, 257, 0)
            keybd_event(20, 0, 2, 0)
        def closing() -> NoReturn:
            keybd_event(20, 0, 256, 0)
            keybd_event(20, 0, 2, 0)
        def beeping() -> NoReturn:
            x: int = round(t * 1000) if i == '.' else round(t * 3000) if i == '-' else 0
            winsound.Beep(440, x)
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
        for i, j in zip(encoded, tmp):
            if i == '.':
                opening()
                #time.sleep(t)
                winsound.Beep(440, round(t*1000))
                self.unreal += t
                self.cnt = "Fuck! "
                closing()
                sleeping()
                self.unreal += countsleep()
                self.cnt = "Nyancat! "
            elif i == '-':
                opening()
                #time.sleep(3*t)
                winsound.Beep(440, round(t*3000))
                self.cnt = 3*t
                self.unreal += 3*t
                closing()
                sleeping()
                self.cnt = "Fuck! "
                self.unreal += countsleep()
        sys.stdout.write('\r100%%[%s] %.2f done.       '%("="*120, time.time()-self.start))
        print()
if __name__ == "__main__":
    a = new(testword)
    a.shine(testword)