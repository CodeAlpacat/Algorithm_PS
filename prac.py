from collections import deque
import math
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

M = 6
N = 6
board_A = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def solution(m, n, board):
    answer = 0
    #2*2 블록 방문처리 => 다시 순회하며 해당하는 인덱스 pop
    #반복 => 방문된 2*2블록이 없다면 break
    for i in range(len(board)):
        board[i] = list(board[i])
    
    visited = [[0] * n for _ in range(m)]
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    for i in range(m):
        for j in range(n):
            cnt = 0
            for k in range(3):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == board[i][j]:
                    cnt += 1
            if cnt == 3:
                visited[i][j], visited[i+1][j], visited[i][j+1], visited[i+1][j+1] = 1
            
            
    

    
            
    return board

print(solution(M, N, board_A))