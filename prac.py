from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

def snail():
    x = 0
    y = 0
    direction = 0
    for i in range(N*N):
        snail_arr[x][y] = i + 1 # 1부터 시작해야함
        #좌표를 이동하기
        x += dx[direction]
        y += dy[direction]
        #이동한 곳이 숫자를 넣을 수 있는 곳일까?
        # if 0 > x or x >= N or 0 > y or y >= N or snail_arr[x][y]:
        if 0 <= x < N and 0 <= y < N and not snail_arr[x][y]: #
            continue
        else:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction + 1) % 4 # 우 하 좌 상 1 2 3 0 1 2 3 3
                                            # 0  1  2  3  방향은 4번인덱스가 없음
            x += dx[direction]
            y += dy[direction]



T = int(input())

for tc in range(T):
    N = int(input())
    snail_arr = [[0] * N for _ in range(N)]
    direction = 0
    snail()
    
    print(f'#{tc+1}')
    for i in snail_arr:
        print(*i)