# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

# N = int(input())
# start = math.floor(math.sqrt(N))
# memo = [[-1] * (N + 1)  for _ in range(start+1)]
# def dp(cur, total):
    
#     if cur < 0:
#         return 0xffffff
#     # 
#     if total > N:
#         return 0xffffff
    
#     if total == N:
#         return 0
    
#     if memo[cur][total] != -1:
#         return memo[cur][total]

#     memo[cur][total] = min(dp(cur + 1, total + cur ** 2) + 1, dp(cur - 1, total))
#     return memo[cur][total]

# print(dp(start, 0))
n = int(input())
d = [0] * (n + 1)
d[0], d[1] = 0, 1

for i in range(2, n + 1):
    minValue = 1e9
    j = 1
    while (j ** 2) <= i:
        minValue = min(minValue, d[i - (j ** 2)])
        j += 1
    d[i] = minValue + 1

print(d[n])