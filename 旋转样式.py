# emerge 样式
import os, sys
from random import choice
e = '|/-\\'
for i in range(1<<20):
    sys.stdout.write("\r%s"%choice(e))

# zypper 样式（只考虑旋转部分，不考虑配合）
import time
for i in range(1<<20):
    # i % 4 = i & 3
    sys.stdout("\r%s"%e[i&3]); time.sleep(1) # 我也不太清楚睡多久QAQ

# 一定要学多线程/多进程！
