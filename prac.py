# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

# input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())

set_M = []
cnt = 0
for i in range(M):
    if input() in S:
        cnt += 1
print(cnt)