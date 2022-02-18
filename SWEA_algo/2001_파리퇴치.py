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


#5 2 N M
#0 1 2 3 4 인덱스
#1 3 3 6 7
#8 13 9 12 8
#4 16 11 12 6
#2 4 1 23 2
#9 13 4 7 3

#1 3     
#8 13 ~    
# 가로세로 0:M / 최종값은 N-M+1까지해야 끝까지 비교
