T = int(input())


for t in range(T):
    N = int(input())
    li = [list(map(int, list(input()))) for _ in range(N)]
    
    mid = N // 2
    s = mid
    e = mid
    ans = 0
    for i in range(N):
        if i <= N//2: # 7일때, 3까지는 증가
            for j in range(s, e+1): #mid까지 range(3, 4) -> (2, 5) -> (1, 6)
                ans += li[i][j]
            if i == N//2:
                pass
            else: 
                s -= 1
                e += 1
        else:# s = 0 e = 6
            s += 1
            e -= 1
            for j in range(s, e+1): #
                ans += li[i][j]
        
    
    print(f'#{t+1} {ans}')