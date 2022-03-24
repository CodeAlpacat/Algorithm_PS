import copy


N = int(input())# 맵 크기
K = int(input())# 사과 수
arr = [[0] * (N+1) for _ in range(N+1)]
for i in range(K):
    a, b = map(int, input().split())
    arr[a][b] = 1 #사과는 1

q = int(input())
rotate = []
for i in range(q):
    a, b = input().split()
    
    rotate.append([int(a), b])
    
snake = [[1, 1]]
arr[1][1] = 2 #뱀 = 2
direction = 0
idx = 0

t = 0 # 초
#     우 하 좌  상      
dx = [0, 1, 0, -1] # 좌회전 0 -> 3 -> 2 -> 1 (direction + 3) % 4
dy = [1, 0, -1, 0] # 우회전 0 -> 1 -> 2 -> 3 (direction + 1) % 4
while True:
    if idx < q and rotate[idx][0] == t:
        if rotate[idx][1] == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4
        
        idx += 1
    
    nx = snake[0][0] + dx[direction]
    ny = snake[0][1] + dy[direction]

    if not (1 <= nx <=N and 1 <= ny <= N) or arr[nx][ny] == 2: #범위 밖 or 자기 몸 부딪힘.
        break
    
    if arr[nx][ny] == 1:
        snake.append([]) #자기 몸의 좌표 늘리기
    else:
        arr[snake[-1][0]][snake[-1][1]] = 0 #꼬리가 지나간 자리 삭제
    
    for i in range(1, len(snake)):
        snake[i] = copy.deepcopy(snake[i - 1]) #리스트 딥카피

    snake[0] = [nx, ny] #다음 지점으로 이동.
    arr[nx][ny] = 2 

    t += 1

print(t + 1)

