from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq


def bfs(start, end):
    visited[start] = mat[start]
    q = deque()
    q.append(start)
    while q:
        n = q.popleft()
        
        if n == end:
            return visited[n]

        for i in graph[n]:
            if visited[i]:
                continue
            
            q.append(i)
            visited[i] = int(str(visited[n]) + str(mat[i])) % 1000000007

    return visited[end]


N, Q = map(int, input().split()) #집, 놀이횟수
mat = [0] + list(map(int, input().split())) #대문에 적힌 수
graph = [[] for _ in range(N+1)]

for i in range(N-1): #도로 정보
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(Q):
    s, e = map(int, input().split()) #시작과 끝 점
    visited = [0] * (N+1)
    print(bfs(s, e))