# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

carved_str = input()

N = int(input())

cnt = 0
for tc in range(N):
    slot = list(input())
    for i in range(10):
        if ''.join(slot[:len(carved_str)]) == carved_str:
            cnt += 1
            break
        slot.append(slot.pop(0))
           
print(cnt)
