N = int(input())
mat = list(map(int, input().split()))


# def recur(cur, cnt):
#     global ans

#     if cur == N:
#         return

#     if cnt + mat[cur] < cnt:
#         ans = max(ans, cnt)

#     recur(cur + 1, cnt + mat[cur])
#     recur(cur + 1, 0)

# ans = -0xffffff
# recur(0, 0)

dp = [0] * len(mat)
dp[0] =mat[0]

for i in range(1, len(mat)):
    dp[i] = max(mat[i], dp[i-1] + mat[i])

print(max(dp))