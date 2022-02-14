#달팽이 숫자
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

list_result = []    
for x in range(T):
    N = int(input())
    li_N = [[0]*N for i in range(N)]
    i_x = 0
    i_y = 0
    cnt = 2 # 방향 벡터 오른쪽
    #사방을 탐색X 첫 줄에서 위쪽이나 왼쪽으로 벗어나면 방향 꺾어버림
    for i in range(N*N):
        li_N[i_x][i_y] = i + 1
        i_x += dx[cnt]
        i_y += dy[cnt]
            #범위를 벗어나는 순간 방향 바꿈.
            #0이 아닌 값이 들어있으면 방향 바꿈(달팽이 안쪽 고려)
        if 0 > i_x or i_x >= N or 0 > i_y or i_y >= N or li_N[i_x][i_y] != 0:
            i_x -= dx[cnt]
            i_y -= dy[cnt] #범위 벗어나니까 원위치
            
            if cnt == 1: #방향 인덱스 1 -> 3 -> 0 -> 2 -> 1
                cnt = 3
            elif cnt == 3:
                cnt = 0
            elif cnt == 0:
                cnt = 2
            elif cnt == 2:
                cnt = 1
            #우 -> 하 -> 좌 -> 상
            i_x += dx[cnt]
            i_y += dy[cnt]
    list_result.append(li_N)

for i in range(len(list_result)):
    print(f'#{i+1}')
    for j in list_result[i]:
        print(*j)
    