# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N = int(input())


mat = []
def recur(cur):

    if cur == N+1:
        print(*mat)
        return
    
    for i in range(1, N+1):
        if i in mat:
            continue
        
        mat.append(i)
        recur(cur + 1)
        mat.pop()

recur(1)