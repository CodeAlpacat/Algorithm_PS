# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
# from collections import deque

# input = sys.stdin.readline

while True:
    try:
        N = int(input())
    except:
        break

    cnt = 0
    ans = 1
    while True:
        
        cnt = cnt * 10 + 1
        cnt %= N
        if cnt == 0:
            print(ans)
            break
        ans += 1