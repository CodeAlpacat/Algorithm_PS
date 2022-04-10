N = int(input())
memo = [-1] * (1000010)

memo[0] = 0
memo[1] = 1
memo[2] = 2 # memo[3] = 2  memo[4] = 5
for i in range(3, N+1):
    memo[i] = (memo[i-1] + memo[i-2]) % 15746
print(memo[N])



###############


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100)
def recur(cur, cnt):
    if cur > N:
        return 0

    if cur == N:
        if cnt == 1:
            return 0
        else:
            return 1

    if memo[cur][cnt] != -1:
        return memo[cur][cnt]                
    
    memo[cur][cnt] = (recur(cur + 1, cnt + 1)+recur(cur + 2, cnt)) % 15746 
    return memo[cur][cnt]

N = int(input())
memo = [[-1] * (N+1) for _ in range(N+1)]
print(recur(0, 0))

##########################

num = int(input())
memo = {1:1, 2:1, 3:2}

def recur(num):
    if num in memo:
        return memo[num]
    if num % 2 == 0:
        a = (recur(num//2) % 15746) * ((recur(num//2) + 2 * recur(num//2 - 1)) % 15746)
    else:
        a = (recur(num//2 + 1) % 15746) ** 2 + (recur(num//2) % 15746) ** 2
    memo[num] = a
    return a
    
print(recur(num+1) % 15746)