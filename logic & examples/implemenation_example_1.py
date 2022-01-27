#상하좌우
#첫줄에 공간의 크기 N * N 을 나타내는 N 입력!
#둘째줄에 A가 이동할 계획을 공백단위로 입력!
#최종 도착좌표 (X, Y)를 공백단위로 출력
#시작위치 = (1,1)
# N = int(input())
# A_move = list(input().split())
# #travel_map =[[i for i in range(1, N+1)] for j in range(1, N+1)]

# # 만약 배열 밖을 벗어나는 범위 예외처리
# #A의 현재 위치
# A_x = 1
# A_y = 1
# for i in A_move:
#     if i == 'R':
#         if A_x == N:
#             pass
#         else:
#             A_x += 1
#     if i == 'U':
#         if A_y == 1:
#             pass
#         else:    
#             A_y -= 1
#     if i == 'D':
#         if A_y ==N:
#             pass
#         else:
#             A_y += 1
#     if i == 'L':
#         if A_x == 1:
#             pass
#         else:
#             A_x -= 1
    

# print(f'{A_y} {A_x}')

# 입력받기
n = int(input())
x, y =1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        nx = x + dx[i]
        ny = y + dy[i]
    #공간을 벗어나면 무시함.
    if nx <1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
    
