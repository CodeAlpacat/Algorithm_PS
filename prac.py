# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [0 for i in range(N+1)]
cnt = {}

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i]

ans = 0
for i in range(N+1):
    # ans += cnt[prefix[i]-M]
    ans += cnt.get(prefix[i]-M, 0)

    cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1

print(ans)