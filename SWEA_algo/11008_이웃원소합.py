T = int(input())
result_list = []
for x in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for i in range(N)]
    
    max_num = 0
    x_max = 0
    y_max = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(N):
            li_max = 0 #초기값
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < N and 0 <= y < N:
                    li_max += li[x][y] # 이웃 전부 더함.
            if li_max > max_num:
                max_num = li_max
                x_max = i
                y_max = j
            
    
    result_list.append([x_max, y_max, max_num])
    
for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i][0]} {result_list[i][1]} {result_list[i][2]}')