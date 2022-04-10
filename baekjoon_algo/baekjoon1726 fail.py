from collections import deque
import heapq
import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
x, y, dir = map(int, input().split())
ex, ey, edir = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
change_dir = [0, 1, 3, 0, 2]

x -= 1
y -= 1
dir = change_dir[dir]

ex -= 1
ey -= 1
edir = change_dir[edir]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

que = deque()
visited = [[[False for i in range(5)] for j in range(m)] for i in range(n)]

d = 0
que.append([x, y, dir])
visited[x][y][dir] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, dir = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if x == ex and y == ey and dir == edir:
            print(d)
            exit()

        # 현재 상태 (x, y, dir)에서 다음 상태는 우선 세칸 전진하는 경우들이 있습니다.
        # 중간에 벽에 막히면 거기부턴 못가는 상태입니다.
        for i in range(1, 4):
            nx = x + i * dx[dir]
            ny = y + i * dy[dir]

            if not in_range(nx, ny) or arr[nx][ny] == 1:
                break

            if visited[nx][ny][dir]:
                continue

            que.append([nx, ny, dir])
            visited[nx][ny][dir] = True

        # dx, dy를 교차하도록 만든다면 (dir + 1) % 4와 (dir + 3) % 4가 좌회전과 우회전을 의미합니다. (x, y, ndir)도 마찬가지로 가능한 다음 상태입니다.
        ndir = (dir + 1) % 4
        if not visited[x][y][ndir]:
            que.append([x, y, ndir])
            visited[x][y][ndir] = True

        ndir = (dir + 3) % 4
        if not visited[x][y][ndir]:
            que.append([x, y, ndir])
            visited[x][y][ndir] = True

    d += 1