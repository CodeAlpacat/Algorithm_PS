# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

#1개를 X원 
#3개를 Y원

# 1
X, Y, N = map(int, input().split())
n, mode = divmod(N, 3)
res = n * Y + mode * X

if 3 * X < Y:
    print(N * X)
else:
    print(res)


#2
N, M, T = map(int, input().split())
mat = [0] * 2 + list(map(int, input().split()))
li = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    li[a] = b
    
for i in range(2, N+1):
    if T > 0:
        T -= mat[i]
    if T <= 0:
        print("No")
        break
    T += li[i]
else:
    print("Yes")




#3
H, W = map(int, input().split())
mat = [list(input()) for _ in range(H)]

x = 0
y = 0
cnt = 0
while (0 <= x < H and 0 <= y < W):
    if cnt == 30000:
        x = -10000
        y = -10000
        break
    if mat[x][y] == 'U' and x != 0:
        x -= 1
    elif mat[x][y] == 'D' and x != H:
        x += 1
    elif mat[x][y] == 'L' and y != 0:
        y -= 1
    elif mat[x][y] == 'R' and y != W:
        y += 1

    cnt += 1

if x == H:
    x = H - 1
if y == W:
    y = W - 1
if x == -1:
    x = 0
if y == -1:
    y = 0

if x < -1000 or y < -1000:
    print(-1)
else:
    print(x+1, y+1)