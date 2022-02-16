T = int(input())


for x in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    
    for j in range(N):
        mx_cnt = -1
        cnt = 1
        for i in range(1, N):
            if li[i] > li[i-1]:
               cnt += 1
               if mx_cnt < cnt:
                mx_cnt = cnt
            else:
                cnt = 1 # 1 2 3 2 3 4 5 
        
        
    
    print(f'#{x+1} {mx_cnt}')