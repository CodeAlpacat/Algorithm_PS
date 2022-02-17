# T = int(input())
# for x in range(T):
#     N, M = map(int, input().split())
#     li = list(map(int, input().split())) + [0]
    
#     s = 0
#     e = M-1
#     total = 0
#     total_max = 0
#     for i in range(M):
#         total_max += li[i]
#     while e < N: #N개의 수니까 e가 N에 도달하면 끝.
#         if e - s < M: #구간 3개
#             for j in range(M):
#                 total += li[s+j]
#             if total_max < total:
#                 total_max = total
#             total = 0
#             e += 1
#         else:
            
#             s += 1 #같을 때는 s가 증가해야함.

#     s_2 = 0
#     e_2 = M-1
#     total_2 = 0
#     total_min = 0
#     for i in range(M):
#         total_min += li[i]
#     while e_2 < N: #N개의 수니까 e가 N에 도달하면 끝.
#         if e_2 - s_2 < M: #구간 3개
#             for j in range(M):
#                 total_2 += li[s+j]
#             if total_min > total:
#                 total_min = total
#             total_2 = 0 
#             e_2 += 1
#         else:
             
#             s_2 += 1 #같을 때는 s가 증가해야함.
#     print(f'#{x+1} {total_max-total_min}')

# # 10 3 10개의 수에서 연속된 3개가 최대인 값.
# # 0 1 2 3 4 5 6 7 8 9 인덱스
# # 1 2 3 4 5 6 7 8 9 10
# # s
# #     e
def sum_li(arr):
    total = 0
    for i in arr:
        if type(i) == list:
            for j in i:
                total += j
        else:
            total += i
    return total

arr_1 = [[1, 3, 2, 1, 3], [3, 1, 3, 2, 1], [3, 3, 1, 1, 2], [1, 3, 2, 2, 1], [1, 2, 3, 3, 2]]
arr_2 = arr_1[0:2][0:2]
print(arr_2)