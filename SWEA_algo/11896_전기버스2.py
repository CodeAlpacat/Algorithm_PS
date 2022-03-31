T = int(input())

def recur(cur):
    ret = 1000000000

    if cur >= len(mat):
        return 0

    if memo[cur] != None:
        return memo[cur]

    for i in range(mat[cur]):
        ret = min(ret, recur(cur + i + 1) + 1)
        memo[cur] = ret

    return ret


for tc in range(1, T + 1):
    mat = list(map(int, input().split()))
    mat.pop(0)
    memo = [None] * len(mat)
    print(f'#{tc} {recur(0) - 1}')