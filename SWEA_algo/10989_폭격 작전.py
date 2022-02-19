T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for p in range(T):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    li_cnt = [[0] * N for _ in range(N)]

    for q in range(M):
        bomb_x, bomb_y, power = map(int, input().split())
        li_cnt[bomb_x][bomb_y] += 1

        for i in range(4):
            nx = bomb_x
            ny = bomb_y
            cnt = 0
            while 0 <= nx + dx[i] < N and 0 <= ny + dy[i] < N and cnt < power:
                nx += dx[i]
                ny += dy[i]
                li_cnt[nx][ny] += 1
                cnt += 1
    res = 0
    for i in range(len(li)):
        for j in range(len(li)):
            if li_cnt[i][j] > 0:
                res += li[i][j]

    print(f'#{p+1} {res}')