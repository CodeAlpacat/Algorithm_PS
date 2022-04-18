N = int(input())
ans = ''
def recur(cur, cnt):

    if cur == N:
        if cnt % 2 == 1:
            return 1
        else:
            return 0
    if cur + 1 > N or cur + 3 > N or cur + 4 > N:
        return 0

    if memo[cur][cnt] != None:
        return memo[cur][cnt]

    memo[cur][cnt] = not (recur(cur + 1, cnt + 1)) or not (recur(cur + 3, cnt + 1)) or not (recur(cur + 4, cnt + 1)) 
    return memo[cur][cnt]


memo = [[None]* (N+1) for _ in range(N+1)]

a = recur(0, 0)
if a == 1:
    print('SK')
else:
    print('CY')

##########################

N = int(input())

dp = [False for i in range(1010)]

dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 1

for i in range(5, N+1):
    if (not dp[i-1]) or (not dp[i-3]) or (not dp[i-4]):
        dp[i] = True
    else:
        dp[i] = False

if dp[N]:
    print('SK')
else:
    print('CY')
