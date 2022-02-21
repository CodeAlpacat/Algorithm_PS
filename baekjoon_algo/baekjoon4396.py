# 지뢰찾기
dx = [0, 1, 0, -1, 1, -1, 1, -1]  # 우하좌상, 우하, 우상, 좌하, 좌상
dy = [1, 0, -1, 0, 1, 1, -1, -1]  #

n = int(input())
arr_bomb = [list(input()) for _ in range(n)]
arr_opened = [list(input()) for _ in range(n)]
arr_result = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr_bomb[i][j] == '.' and arr_opened[i][j] == 'x':
            cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 > nx or nx >= n or 0 > ny or ny >= n:  # x이면서 지뢰인 경우는 위에서 처리해줌.
                    continue
                if arr_bomb[nx][ny] == '*':
                    cnt += 1
            arr_result[i][j] = cnt

        if arr_opened[i][j] == 'x' and arr_bomb[i][j] == '*':  # x라 오픈했는데 *이면 모든 별 오픈
            for p in range(n):
                for q in range(n):
                    if arr_bomb[p][q] == '*':
                        arr_result[p][q] = '*'

for i in range(n):
    for j in range(n):
        print(arr_result[i][j], end='')
    print()