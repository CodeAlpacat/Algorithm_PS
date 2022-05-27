from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

# N = int(input())

# arr1 = [i for i in range(N)] # 같음
# #---------------------
# arr2 = []
# for i in range(N): #같음
#     arr2.append(i)

# x = 1
# arr3 = [0 for i in range(N) if x == 0]
# #---------------------
# arr4 = []
# for i in range(N):
#     if x == 0:
#         arr4.append(0)
# # 1 2 3 4 5 
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
 

# arr = [1, 2, 3, 4, 5, 6]

# arr2 = [arr[0:3] for _ in range(3)]

# res = []
# for i in range(3):
#     for j in range(3):
#         res.append(arr[i])

# arr = [list(map(int, input().split())) for _ in range(N)]
# arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]
# #1 2 3
# #4 5 6
# #7 8 9
# (x, y)
# (x+1, y)
# (x, y+1)
# (x+1, y+1)

# dx = [1, 0, 1]
# dy = [0, 1, 1]



# for i in range(3):
#     for j in range(3):
#         result = arr[x][y]
#         for i in range(3):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < 3 and 0 <= ny < 3:
#                 result += arr[nx][ny]



# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)

# (0, 0) (0, 2)
# (0, 1) (1, 2)
# (0, 2) (2, 2)

# (1, 0) (0, 1)
# (1, 1) (1, 1)

# N = 3
# li = [list(map(int, input().split())) for _ in range(N)]

# arr = [[0] * N for _ in range(N)]
# 0, (0 1 2)
# 0 0 / 0 1 / 0 2/
# #결과 = i 자리에 있는 애들이 감소해야함
# #그럼? j에 있는 증가하는 값들을 끝에서부터 빼줌. => 끝? => N-1
# 2 0 / 1 0 / 0 0/

# N - 1 - j
# # (0, 0) (0, 1) (0, 2)
# for i in range(N): # 0
#     for j in range(N): # 0 1 2
#         arr[i][j] = li[N-1-j][i]

# print()
# for i in arr:
#     print(*i) 