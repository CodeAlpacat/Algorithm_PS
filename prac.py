# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N, a, b = map(int, input().split())
mat = []
for i in range(1, N+1):
    mat.append(i)

flag = False
cnt = 1
while len(mat):
    last_man = -1
    if len(mat) % 2 == 1:
        last_man = len(mat)
        mat.pop()
    if len(mat) == 1:
        break
    
    contain_zero = False
    for i in range(0, len(mat), 2):
        if mat[i] == a and mat[i + 1] == b:
            flag = True
            break

        if mat[i] == a:
            mat[i+1] = 0
            contain_zero = True
            continue
        elif mat[i+1] == a:
            mat[i] = 0
            contain_zero = True
            continue

        if mat[i] == b:
            mat[i+1] = 0
            contain_zero = True
            continue
        elif mat[i+1] == b:
            mat[i] = 0
            contain_zero = True
            continue

        mat[i+1] = 0
        contain_zero = True

    if flag:
        break
    if contain_zero:
        mat.remove(0)
    
    if last_man > 0:
        mat.append(last_man)

    cnt += 1

if not flag:
    print(-1)
else:
    print(cnt)