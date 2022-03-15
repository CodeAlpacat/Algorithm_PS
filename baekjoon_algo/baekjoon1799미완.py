# N = int(input())
# chess_map = [list(map(int, input().split())) for _ in range(N)]
# visited = [[-10000] * N for _ in range(N)]
# ans = 0

# # def recur(x, y, cnt):
# #     global ans 
    
# #     if y == N:
# #         x += 1
# #         y = 0
# #     if x == N:
# #         ans = max(ans, cnt)
# #         return

# #     check = bishop_move(x, y, visited)
# #     if check:
# #         visited[x][y] = 2

# #     recur(x, y + 1, cnt + (check == True) * 2)


# def recur(cur, cnt):
    

#     for i in range(cur + 1):
            
            
#             visited[i][j] = 2
#             recur(cur + 1, j + 1)
#             visited[i][j] = -10000


# # 비숍은 대각선 이동 가능. 현재 비숍이 배치된 맵 placed_bishop을 인자로 받음. 비숍이 있는 자리는 2로 표시됨
# def bishop_move(x, y, placed_bishop):
#     dx = [1, 1, -1, -1]
#     dy = [1, -1, 1, -1]
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         while 0 <= nx < N and 0 <= ny < N and chess_map[nx][ny] == 0:
#             if placed_bishop[nx][ny] == 2: #대각선에 2가 있으면 False
#                 return 0
#     else: # 2가 하나도 없었거나 벽에 가로 막혀서 비숍끼리 안겹침.
#         return 1

# recur(0, 0, 0)
# print(ans)



n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
in_range = lambda y, x: 0 <= y < n and 0 <= x < n #x, y가 범위에 있는지


rd = {}  # 우하향(right down) 대각선
# 중앙 기준으로 쁠마
# (y,x) -> rd[x-y], 왼쪽 아래가 -(n-1), 오른쪽 위가 (n-1)
for i in range(-n + 1, n):
    rd[i] = 0  # 초기화

def upper_bound(diag):  # 현재 대각선(우상향) 위치에서부터 끝 대각선까지 뽑힐 가능성이 있는 애들의 갯수 반환
    able_rus = 0  # 가능한 우상향 대각선들의 개수, 실제 가능하다기보단 단순히 가능할수도 있는 애들
    for d in range(diag, 2 * n - 1):
        for y in range(d + 1):
            x = d - y
            if in_range(y, x) and board[y][x] and rd[x - y] == 0:
                able_rus += 1
                break
    return able_rus


def f(diag, cnt):  # diag 은 우상향 대각선의 번호. 첫 우상향 대각선이 0, 마지막이 2*n-2
    global ans
    if diag == 2 * n:
        ans = max(ans, cnt)
        return

    ub = upper_bound(diag)  # 상한, 이번 대각선부터 끝까지 갔을 때 최대로 더 가질 수 있는 값
    if ub + cnt <= ans:  # 현재 cnt 값과 앞으로 최대한 얻을 수 있는 값을 더해도 기존 ans 보다 작으면
        return  # 빠져나온다

    for y in range(diag + 1):  # 현재 대각선에서 가능한 y,x 조합 찾기
        x = diag - y
        if in_range(y, x) and board[y][x] and rd[x - y] == 0:
            rd[x - y] = 1  # 현재 (y,x) 좌표에 비숍 넣었으므로, (y,x)가 속한 우하향 대각선 체크
            f(diag + 1, cnt + 1)  # (y,x) 좌표에 비숍 넣었으므로 cnt+1 하고 다음 우상향 대각선으로 감(diag+1)
            rd[x - y] = 0

    f(diag + 1, cnt)  # 이번 우상향 대각선에서 어떠한 좌표에도 비숍 넣지 않은 경우(cnt 그대로)


ans = 0
f(0, 0)
print(ans)