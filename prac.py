# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

# input = sys.stdin.readline

#-5 -4 -3 -2 -1 0 1 2 3 4 5
#5 4
#1 ~ 9 중심 사이의 거리가 r1 + r2보다

N = int(input())

mat = []
for i in range(N):
    mat.append(list(map(int, input().split())))
    
def check():
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            
            if abs(mat[i][0] - mat[j][0]) <= mat[i][1] + mat[j][1]:
                if mat[i][0]-mat[i][1] >
                return 'NO'
            
            if mat[i][1] > mat[j][1]:
                if mat[i][0] + mat[i][1] > mat[j][0] + mat[j][1] and mat[i][0] - mat[i][1] < mat[j][0] - mat[j][1]:
                    pass
                else:
                    return 'NO'
            elif mat[i][1] < mat[j][1]:
                if mat[j][0] + mat[j][1] > mat[i][0] + mat[i][1] and mat[j][0] - mat[j][1] < mat[i][0] - mat[i][1]:
                    pass
                else:
                    return 'NO'
            else:
                return 'NO'
    else:
        return 'YES'
print(check())