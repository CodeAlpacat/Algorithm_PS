# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N = int(input())
mat = sorted(list(map(int, input().split())))
mat2  = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(N):
    ans += mat[i] * mat2[i]

print(ans)