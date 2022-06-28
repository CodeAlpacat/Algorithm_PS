# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
mat = list(map(int, input().split())) + [0]
s = 0
e = 0
total = mat[0]
cnt = 0
while e < N:
    
    if total < M:
        e += 1
        total += mat[e]
    
    elif total > M:
        total -= mat[s]
        s += 1
    
    else:
        cnt += 1
        e += 1
        total += mat[e]

print(cnt)