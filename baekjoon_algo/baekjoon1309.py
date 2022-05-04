N = int(input())

dp = [0 for i in range(N+1)]
dp[0] = 1
dp[1] = 3
for i in range(2, N+1):
    dp[i] = (dp[i-2] + 2 * dp[i-1]) % 9901


print(dp[N])