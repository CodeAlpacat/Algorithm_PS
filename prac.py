#사다리타기
dx = [0, 0, 1]
dy = [1, -1, 0]
result_list = []

for _ in range(1):
    T = int(input())
    lis = [list(map(int, input().split())) for _ in range(10)]
    
    
    # r가 0행에 도달할 때까지 무한 반복
    for j in range(10):
        for i in range(10):
            if lis[9][i] == 2:
                n = i # 90번대
        y = j
        x = 0
        idx = 0
        while x < 10:
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < 10 and 0 <= ny < 10:  # out of index 에러 방지
                # 세 가지 방향 중에 1이 있다면 그쪽으로 이동
                if lis[nx][ny] == 1:
                    x = nx
                    y = ny
                    lis[nx][ny] = False  # 붕섀
            idx = (idx + 1) % 3

        if y == j:
            print(y)
            break
    
    
    # 도착지점

 # 마지막 i는 시작 지점 좌표  

# for i in range(len(result_list)):
#

# 1
# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 1 1 1
# 1 0 0 0 1 0 1 0 0 1
# 1 1 1 1 1 0 1 0 0 1
# 1 0 0 0 1 1 1 0 0 1
# 1 0 0 0 1 0 1 0 0 2
