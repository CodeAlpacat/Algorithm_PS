# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
        
cnt = 1
def dfs(v):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if visited[i]:
            continue
        cnt += 1
        dfs(i)

dfs(R)
for i in visited[1:]:
    print(i)