# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

mat = []
total_spy = -100
for i in range(9):
    N = int(input())
    mat.append(N)
    total_spy += N

mat.sort()
s = 0
e = 8

while s < e:
    
    if mat[s] + mat[e] < total_spy:
        s += 1
    elif mat[s] + mat[e] > total_spy:
        e -= 1
    else:
        break

for i in range(len(mat)):
    if i == s or i == e:
        continue
    print(mat[i])

    