from collections import deque
import math
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq


#에라토스테네스의 체
#청기 True 백기 False

N = int(input())

flags = [False for _ in range(N+1)] # 2부터 시작. 1에서는 이미 뒤집음

for i in range(2, N+1):

    for j in range(i, N+1, i):
        flags[j] = not flags[j]


cnt = 0
for i in range(1, N+1):

    if not flags[i]:
        cnt += 1

print(*flags)