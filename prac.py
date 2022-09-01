# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys

def dfs(v):
    for i in range(N):
        if not visited[i] and graph[v][i]:
            visited[v] = True   
            dfs(i)

#1 2 3
#1 2
#2 3
#1 3

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N)

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0] * N
