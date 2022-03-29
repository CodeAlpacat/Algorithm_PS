def check():
    cnt = 1
    next = arr[0][1]
    for i in range(1, N):
        if next <= arr[i][0]:
            cnt += 1
            next = arr[i][1]
    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    li = []
    arr.sort(key=lambda x: x[1])
    
    print(f'#{tc} {check()}')

##########
T = int(input())

def recur(cur):
        if dp[cur] != -1:
            return dp[cur]
        
        ret = 0
        
        for i in range(n):
            if cur <= arr[i][0]:
                ret = max(ret, recur(arr[i][1]) + 1)
                dp[cur] = ret
                
        return ret

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [-1 for _ in range(25)]
    
    print(f'#{tc} {recur(0)}')