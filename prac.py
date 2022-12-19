# sys.stdin=open('sample_input.txt')
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
mat.sort(key=lambda x: x[1])
total = 0
min_time = 0xffffff
for i in range(N):
    total += mat[i][0]
    min_time = min(min_time, mat[i][1]-total)
    if total > mat[i][1]:
        print(-1)
        exit()
    

print(min_time)