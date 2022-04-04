
def bfs(v):
    visited = [False] * (N+1)
    q = [v]
    visited[v] = True
    while q:

        for _ in range(len(q)):
            n = q.pop(0)
            
            for i in graph[n]:
                if visited[i]:
                    continue
                q.append(i)
                visited[i] = visited[n] + 1
    return max(visited) - 1

N = int(input())
graph = [[] for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    
    if a == -1 and b == -1:
        break

    graph[a].append(b)
    graph[b].append(a)


li = []
min_num = 100000000

for i in range(1, N+1):
    ans = bfs(i)
    li.append(ans)
    if ans <= min_num:
        min_num = ans

cnt = 0
res = []
for i in range(len(li)):
    if min_num == li[i]:
        res.append(i+1)
        cnt += 1

print(min_num, cnt)
print(*res)