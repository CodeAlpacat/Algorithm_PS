# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

#시작 좌표나 Sii만 아니면 비교한 뒤 절대 값 비교
#i < j 여야함


N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
ans = 0xffffff



start_link = []
for i in range(N):
    for j in range(i, N):
        if i != j:
            start_link.append(mat[i][j] + mat[j][i])

for i in range(len(start_link)):
    for j in range(i, len(start_link)):
        if i < j:
            ans = min(ans, abs(start_link[j] - start_link[i]))
        
print(ans)
print(start_link)
#5, 9, 6, 6, 10, 7