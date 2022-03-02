#돌게임 3
#시간초과
N = int(input())
memo = [-1] * 1010
ans = ''
def recur(cur, cnt):
    global ans
    
    
    if cur == N:
        if cnt % 2 == 1:
            ans = 'SK'
            return
        else:
            ans = 'CY'
            return
    if cur + 1 > N or cur + 3 > N or cur + 4 > N:
        return
    recur(cur + 1, cnt + 1)
    recur(cur + 3, cnt + 1)
    recur(cur + 4, cnt + 1)

recur(0, 0)
print(ans)

#상향식
N = int(input())

dp = [False for i in range(1010)]

dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, N+1):
    if (not dp[i-1]) or (not dp[i-3]) or (not dp[i-4]):
        dp[i] = True
    else:
        dp[i] = False

if dp[N]:
    print('SK')
else:
    print('CY')