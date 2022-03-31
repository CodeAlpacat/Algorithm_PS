def recur(cur, cnt):
    global ans
    if cur > N:
        return

    if cur == N:
        ans = min(ans, cnt)
        return

    if cnt > ans:
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        recur(cur + 1, cnt + mat[cur][i])
        visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N  = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * len(mat)
    ans = 1000000000
    recur(0, 0)
    print(f'#{tc} {ans}')