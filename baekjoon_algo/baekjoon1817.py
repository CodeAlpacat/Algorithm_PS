N, M = map(int, input().split())

if N == 0:
    print(0)
else:    
    mat = list(map(int, input().split()))
    cnt = 0
    total = 0
    i = 0
    for i in range(N):

        if total + mat[i] > M:
            cnt += 1
            total = 0
        total += mat[i]

            
    print(cnt+1)