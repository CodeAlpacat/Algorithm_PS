# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline


N, S = map(int, input().split())

mat = []
for i in range(N):
    mat.append(int(input()))
cnt = 0
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        
        if mat[i] + mat[j] <= S:
            cnt += 1

print(cnt)