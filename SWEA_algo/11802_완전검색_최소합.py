def recur(x, y):
    if x > N-1 or y > N-1:
        return 100000000

    if x == N-1 and y == N-1:
        return 0

    if memo[x][y] != -1:
        return memo[x][y]

    memo[x][y] = min(recur(x + 1, y) + mat[x][y], recur(x, y + 1) + mat[x][y])
    return memo[x][y]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1] * N for _ in range(N)]

    print(f'#{tc} {recur(0, 0) + mat[N-1][N-1]}')
###############################################

def recur(x, y, total):
    global ans
    if x > N-1 or y > N-1:
        return

    if x == N-1 and y == N-1:
        ans = min(ans, total)
        return

    recur(x + 1, y, total + mat[x][y])
    recur(x, y + 1, total + mat[x][y])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ans = 1000000000
    recur(0, 0, 0)
    print(f'#{tc} {ans+ mat[N-1][N-1]}')