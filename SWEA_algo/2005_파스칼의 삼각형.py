#파스칼의 삼각형
#백트래킹으로 풀어보기
T = int(input())

for x in range(T):
    N = int(input())
    li = [[0] * N for _ in range(N)]
    li[0][0] = 1
    for i in range(N):
        li[i][0] = 1
        li[i][i] = 1
    
    for i in range(N):
        for j in range(N):
            if li[i][j] != 1:
                li[i][j] = li[i-1][j-1] + li[i-1][j]
    print(f'#{x+1}')
    for i in range(N):
        for j in range(i+1):
            print(li[i][j], end = ' ')
        print()

# ------------------------------------------------- DP 조합
memo = [[0] * 100 for _ in range(100)]

def recur(cur, cnt):
    
    if memo[cur][cnt]:
        return memo[cur][cnt]

    if cur == cnt or cnt == 0:
        memo[cur][cnt] = 1
        return 1

    memo[cur][cnt] = recur(cur - 1, cnt - 1) + recur(cur - 1, cnt) #안고르는 경우
    return memo[cur][cnt]

recur(4, 4)
