#사다리타기
for _ in range(10):
    T = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점
    dx = [0, 0, -1,] # 상
    dy = [1, -1, 0] # 우 좌
    y = 0
    for j in range(100):
        if li[99][j] == 2: #마지막 줄의 도착 지점이 무슨 열인지 저장.
            y = j

    direction = 0
    x = 99
    # x가 0행에 도달할 때까지 무한 반복
    while x > 0:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < 100 and 0 <= ny < 100:  # out of index 에러 방지
            # 세 가지 방향 중에 1이 있다면 그쪽으로 이동
            if li[nx][ny] == 1:
                x = nx
                y = ny
                li[nx][ny] = False #지나온 곳 False로 막아버림
        direction = (direction + 1) % 3

    print(f'#{T} {y}')