list_result = []

for x in range(10):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]
    
    cross_num = 0
    rev_cross_num = 0
    for i in range(len(num_list)): #대각선의 합들
        for j in range(len(num_list)):
            if i == j:
                cross_num += num_list[i][j]
            if i == len(num_list)-1-j:
                rev_cross_num += num_list[i][j]
    #각 행의 최대값 비교
    max_a = 0
    for i in range(len(num_list)):
        max_row = 0
        for j in range(len(num_list)):
            max_row += num_list[i][j]
        if max_row > max_a:
            max_a = max_row
    #각 열의 최대값 비교
    max_b = 0
    for i in range(len(num_list)):
        max_col = 0
        for j in range(len(num_list)):
            max_col += num_list[j][i]
        if max_col > max_b:
            max_b = max_col
    
    list_result.append(max(max_a, max_b, cross_num, rev_cross_num))

for i in range(len(list_result)):
    print(f'#{i+1} {list_result[i]}')