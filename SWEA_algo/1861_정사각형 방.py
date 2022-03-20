from collections import deque
T = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def bfs(x, y):
    ans = 0
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        ans += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny):
                continue
            if (graph[x][y] + 1) != graph[nx][ny]:
                continue
            q.append([nx, ny])
    return ans

            
for tc in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    ans_idx = 0
    for i in range(N):
        for j in range(N):
            a = bfs(i, j)
            if res < a:
                res = a
                ans_idx = graph[i][j]
            elif a == res:
                if graph[i][j] < ans_idx:
                    ans_idx = graph[i][j]
    print(f'#{tc+1} {ans_idx} {res}')