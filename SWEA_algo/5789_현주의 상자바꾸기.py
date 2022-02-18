T = int(input())

for x in range(T):
    N, Q = map(int, input().split())
    li = [0 for i in range(1, N+1)]
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            li[j] = i+1
    
    print(f'#{x+1}', end =' ')
    print(*li)