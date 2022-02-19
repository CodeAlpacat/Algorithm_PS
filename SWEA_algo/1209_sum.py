# list_result = []
#
# for x in range(10):
#     N = int(input())
#     num_list = [list(map(int, input().split())) for _ in range(100)]
#
#     cross_num = 0
#     rev_cross_num = 0
#     for i in range(len(num_list)): #대각선의 합들
#         for j in range(len(num_list)):
#             if i == j:
#                 cross_num += num_list[i][j]
#             if i == len(num_list)-1-j:
#                 rev_cross_num += num_list[i][j]
#     #각 행의 최대값 비교
#     max_a = 0
#     for i in range(len(num_list)):
#         max_row = 0
#         for j in range(len(num_list)):
#             max_row += num_list[i][j]
#         if max_row > max_a:
#             max_a = max_row
#     #각 열의 최대값 비교
#     max_b = 0
#     for i in range(len(num_list)):
#         max_col = 0
#         for j in range(len(num_list)):
#             max_col += num_list[j][i]
#         if max_col > max_b:
#             max_b = max_col
#
#     list_result.append(max(max_a, max_b, cross_num, rev_cross_num))
#
# for i in range(len(list_result)):
#     print(f'#{i+1} {list_result[i]}')
#
for x in range(10):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    max_n = 0
    cross_num = 0
    cross_rev_num = 0
    for i in range(100):
        sum_r = 0 #가로
        sum_c = 0 #세로
        for j in range(100):
            sum_r += li[i][j]
            sum_c += li[j][i]
        if sum_r > max_n:
            max_n = sum_r
        if sum_c > max_n:
            max_n = sum_c

        cross_num += li[i][i]
        cross_rev_num += li[i][N-1-i]

    if max_n < cross_num:
        max_n = cross_num
    if max_n < cross_rev_num:
        max_n = cross_rev_num

    print(f'#{x+1} {max_n}')