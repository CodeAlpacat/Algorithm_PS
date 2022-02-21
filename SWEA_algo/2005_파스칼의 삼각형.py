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