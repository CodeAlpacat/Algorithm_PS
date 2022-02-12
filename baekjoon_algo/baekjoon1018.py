# #체스판 다시 칠하기

# N, M = map(int, input().split())
# chess_map = []
# for _ in range(N):
#     chess_map.append(list(input()))
# # 10 13

# list_count = []

# for i in range(N-7): # 0, 1, 2, 3, 4 y축
#     for j in range(M-7): # 0, 1 x축
#         count_B = 0
#         count_W = 0
#         for k in range(8): #y축 8번
#             for m in range(8): # x축으로 8번
#                 if (i+k+j+m) % 2 == 0:
#                     if chess_map[i+k][j+m] != 'W':
#                         count_B += 1
#                     if chess_map[i+k][j+m] != 'B':
#                         count_W += 1
#                 else:
#                     if chess_map[i+k][j+m] != 'B':
#                         count_B += 1
#                     if chess_map[i+k][j+m] != 'W':
#                         count_W += 1
#         list_count.append(min(count_B, count_W))

# print(min(list_count))

# 체스판 다시 칠하기

N, M = map(int, input().split())
chess_map = []
for _ in range(N):
    chess_map.append(list(input()))

list_count = []

for i in range(N-7): # 0, 1, 2, 3, 4 y축
    for j in range(M-7): # 0, 1 x축
        count = 0
        first_color = chess_map[i][j]
        for k in range(8): #y축 8번
            for m in range(8): # x축으로 8번
                if chess_map[i+k][j+m] != first_color:
                    count += 1
                
                if first_color == 'B':
                    first_color = 'W'
                else:
                    first_color = 'B'
                # 뒤바꿔줘야함.
            if first_color == 'B':
                first_color = 'W'
            else:
                first_color = 'B'
                # 제자리로
        list_count.append(count)

print(min(list_count))