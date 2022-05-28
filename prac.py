from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

#가로 검증 / 몇 번째 줄인지 확인
def check_hori(x):
    list_number = []
    for i in range(9):
        list_number.append(sudoku_map[x][i])
    
    if len(set(list_number)) == 9:
        return True
    else:
        return False

#세로 검증
def check_vert(y):
    list_number = []
    for i in range(9):
        list_number.append(sudoku_map[i][y])
    
    if len(set(list_number)) == 9:
        return True
    else:
        return False

#현재 범위에 속한 3*3 박스를 검증한다.
def check_box(x, y): # x, y를 입력받는다
    x -= (x % 3) #반복의 시작 x 좌표
    y -= (y % 3) #반복이 시작하는 y 좌표
    list_number = [] #검증할 리스트
    for i in range(x, x+3): #시작 좌표에서 시작좌표 + 2까지 검증해야한다. 0 1 2
        for j in range(y, y+3):
            list_number.append(sudoku_map[i][j])
    
    if len(set(list_number)) == 9:
        return True
    else:
        return False

def get_result():
    for i in range(9):
        for j in range(9):
            if not (check_hori(j) and check_vert(i) and check_box(i, j)):
                return 0
    return 1
                
T = int(input())

for tc in range(T):
    sudoku_map = [list(map(int, input().split())) for _ in range(9)] # 9 * 9 스도쿠 지도
    print(f'#{tc+1} {get_result()}')