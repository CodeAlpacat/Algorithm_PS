from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

N = int(input())
par = [0] * (N+1)
v = [[] for _ in range(N+1)]

for i in range(N-1):
    p, c, d = map(int, input().split())
    v[c].append([p, d])
    v[p].append([c, d])


def dfs(cur, prv):
    for nxt in v[cur]:
        if nxt[0] == prv:
            continue
        par[]
        dfs(nxt, cur)