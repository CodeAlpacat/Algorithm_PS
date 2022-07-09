# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

#지구 태양 달
#E S M
#15 28 19

E, S, M = map(int, input().split())
A, B, C = 1, 1, 1

cnt = 1

while E != A or S != B or M != C:
    A += 1
    B += 1
    C += 1
    
    if A == 16:
        A = 1
    if B == 29:
        B = 1
    if C == 20:
        C = 1
    cnt += 1

print(cnt)