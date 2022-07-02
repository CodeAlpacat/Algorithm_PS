T = int(input())

for x in range(T):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for i in range(N)]
    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(i, M+i): #i =0, j = 1 => 0,1 0,2 1,1, 1,2
                for p in range(j, M+j): # i = 0 j = 2 => 0,2 0,3 1,2, 1,3
                    total += li[k][p]
            if max_num < total:
                max_num = total
    
    print(f'#{x+1} {max_num}')

