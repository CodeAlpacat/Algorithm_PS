# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

# input = sys.stdin.readline

N, K = map(int, input().split())
mat = list(map(int, input().split()))
children = []

res = 0
cnt = 0
for i in range(1, len(mat)):
    children.append(mat[i] - mat[i-1])

children.sort()
new_li = []
for i in range(len(children)):
    
    if i == N - K:
        break

    res += children[i]

print(res)