T = int(input())

def recur(cur, used):
    ret = -1000000000
    if cur > N:
        return 0

    if cur == N:
        return 1

    for i in range(N):
        if used & (1 << i):
            continue
        ret = max(recur(cur + 1, used|(1<<i)) * mat[cur][i]/100, ret)
    return ret

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * len(mat)
    recur(0, 100)
    print(f'#{tc} {ans:6f}')


#################################

T = int(input())

def recur(cur, cnt):
    global ans

    if cnt < ans:
        return

    if cur > N:
        return

    if cur == N:
        ans = max(ans, cnt)
        return

    for i in range(N):
        if visited[i] or mat[cur][i] == 0:
            continue

        visited[i] = True
        recur(cur + 1, cnt * mat[cur][i] / 100)
        visited[i] = False


for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    memo = [None] * (len(mat) + 1)
    visited = [0] * len(mat)
    ans = -1000000000
    recur(0, 100)
    print(f'#{tc} {ans:6f}')