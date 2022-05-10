from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

N = int(input())
mat = list(map(int, input().split()))

def recur(cur, cnt):
    global ans
    if cur > N:
        return
    
    if cur == N:
        ans = max(ans, cnt)
        return
    

    if mat[cur] < 0:
        recur(cur + 1, cnt)
    recur(cur + 1, cnt + mat[cur])

ans = -0xffffff
recur(0, 0)
print(ans)