
import sys
sys.setrecursionlimit(10000)

def recur(cur, prv):
    ret = 0xffffff
    if cur > N or prv > 3:
        return 0xffffff

    if cur == N:
        return 0

    if memo[cur][prv] != -1:
        return memo[cur][prv]

    for i in range(3):
        if prv == i:
            continue
        ret = min(ret, recur(cur + 1, i) + mat[cur][i])
        memo[cur][prv] = ret
    return ret

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
memo = [[-1] * (N+10) for _ in range(N+10)]

print(recur(0, 18))


##############################################################################

N = int(input())
mat = [[0] * 3] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(3):
        mn = 0xffffff
        for k in range(3):
            if j == k:
                continue

            mn = min(mn, dp[i-1][k])
        dp[i][j] = mn + mat[i][j]
print(min(dp[N]))

# min(recur(i - 1, j), recur(i - 1, j-1), recur(i - 1, j-2))


