# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

def check(n):
    str_n = str(n)
    set_n = set(str(n))
    if len(set_n) != len(str_n):
        return 0
    else:
        return 1

while True:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for i in range(N, M+1):
            cnt += check(i)
        print(cnt)
    except:
        exit()