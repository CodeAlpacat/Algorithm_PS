# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat = [0] +  list(map(int, input().split()))
prefix = [0 for _ in range(N+1)]

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + mat[i]

ans = -0xffffff
for i in range(M, N+1):
    ans = max(ans, prefix[i] - prefix[i-M])

print(ans)