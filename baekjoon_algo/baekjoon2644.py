#촌수계산

from collections import deque


def bfs(v, e):
    q = deque()
    q.append(v)
    visited[v] = True
    d = 0
    while q:
        size = len(q)
        
        for _ in range(len(q)):

            n = q.popleft()
            
            if n == e:
                return d

            for i in graph[n]:
                if visited[i]:
                    continue
                
                q.append(i)
                visited[i] = True
        d += 1
    return -1
n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

print(bfs(start, end))

#7 3
#부모 자식 간의 관계
#0
#1 - 2 3
#2 - 1 7 8 9
#3 - 1
#4 - 5 6
#5 - 4
#6 - 4
#7 - 2
#8 - 2
#9 - 2