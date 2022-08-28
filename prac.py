# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def location(flst):
    lst = flst[:]
    for k in range(len(lst)):
        for i in range(N):
            for j in range(N):    
                if mat[i][j] == lst[k]:
                    lst[k] = [i, j]
    return lst

def bfs(x, y, end_x, end_y):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 0
    q = deque()
    q.append([x, y])
    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    
    for j in range(N):
        for k in range(N):
            if j == end_x and k == end_y:
                return visited[j][k]


def check_distance(lst):
    new_list = [[0, 0]] + location(lst)
    res = 0
    for i in range(1, len(new_list)):
        res += bfs(new_list[i-1][0], new_list[i-1][1], new_list[i][0], new_list[i][1])
    return res

def recur(cur):
    global answer

    if cur == max_num * 2:
        #여기서 check
        # answer = min(answer, check_distance(monster))
        if answer >= check_distance(monster):
            answer = check_distance(monster)
        return

    for i in range(1, max_num+1):
        if i in monster and (-i) in monster:
            continue
        
        # 몬스터를 잡았는데 고객에게 보고 안한 경우
        if i in monster and (-i) not in monster:
            monster.append(-i)
            recur(cur + 1)
            monster.pop()

        #몬스터를 못 잡은 경우
        elif i not in monster:
            monster.append(i)
            recur(cur+1)
            monster.pop()



for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # 몬스터와 헌터 배열
    max_num = -0xffffff
    for i in range(N):
        for j in range(N):
            max_num = max(max_num, mat[i][j])

    monster = []
    answer = 0xffffff
    recur(0)
    print(answer)
    