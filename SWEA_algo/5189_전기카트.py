def recur(x, y,total):
    global ans

    if x > N:
        return

    if x == N:
        total += mat[y][0]
        if total < ans:
            ans = total
            return

    if total > ans:
        return

    for i in range(1, N):
        if not mat[y][i] or visited[i]:
            continue

        visited[i] = True
        recur(x + 1, i, total + mat[y][i])
        visited[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 1000000000

    recur(1, 0, 0)
    print(ans)