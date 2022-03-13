from re import S


R, C, T = map(int, input().split()) #R 세로 C 가로 T 시간
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
cleaner_location_x = []

for i in range(R):
    if graph[i][0] == -1:
        cleaner_location_x.append(i) #공기청정기 좌표

dx = [-1, 0, 1, 0] # 상우하좌(거꾸로 버블 1회 = 한 칸씩 뒤로 미뤄짐.)
dy = [0, 1, 0, -1]

dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]
def dust(graph):
    new_visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] // 5  > 0 : # 5로 나눠 1이상이 아니면 확산되지 않음.
                cnt = 0 # 확산이 가능한 방향 수
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        new_visited[nx][ny] += graph[i][j] // 5
                        cnt += 1
                graph[i][j] -= (graph[i][j] // 5) * cnt
    
    for i in range(R):
        for j in range(C):
            graph[i][j] += new_visited[i][j]

    cleanerUp(cleaner_location_x, graph)
    cleanDown(cleaner_location_x, graph)

def cleanerUp(cleaner_loc, n_visited):
    n_visited[cleaner_loc[0]-1][0] = 0
    x = cleaner_loc[0]-1
    y = 0
    for i in range(4):    
        while 0 <= x +dx[i] <= cleaner_loc[0] and 0 <= y + dy[i] < C and graph[x +dx[i]][y + dy[i]] != -1:
            n_visited[x][y], n_visited[x + dx[i]][y + dy[i]] = n_visited[x + dx[i]][y + dy[i]], n_visited[x][y]
            x += dx[i]
            y += dy[i]
def cleanDown(cleaner_loc, n_visited):
    n_visited[cleaner_loc[1]+1][0] = 0
    x = cleaner_loc[1] + 1
    y = 0
    for i in range(4):    
        while cleaner_loc[1] <= x +dx2[i] < R and 0 <= y + dy2[i] < C and graph[x +dx2[i]][y + dy2[i]] != -1:
            n_visited[x][y], n_visited[x + dx2[i]][y + dy2[i]] = n_visited[x + dx2[i]][y + dy2[i]], n_visited[x][y]
            x += dx2[i]
            y += dy2[i]
for i in range(T):
    dust(graph)
print()
for i in range(R):    
    print(*graph[i])

ans = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            ans += graph[i][j]

print(ans)


# 0 0 0 0 0 1 8 6
# 0 0 1 0 3 0 5 5
# 0 0 2 1 1 0 4 6
# 0 0 5 2 0 0 2 12
# 0 1 1 0 5 10 13 0
# 0 1 9 4 3 5 12 8
# 8 17 8 3 4 8 4 0

# 0 0 0 0 0 2 7 6
# 0 0 1 0 3 1 4 5
# 0 0 3 1 1 1 2 7
# 0 1 1 3 1 2 8 8
# 0 1 3 2 4 7 7 3
# 1 5 8 3 3 9 9 6
# 9 11 7 4 5 5 6 3