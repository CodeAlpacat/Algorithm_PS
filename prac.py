# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N = int(input())

for i in range(N):
    stack = []
    
    M = input()
    for j in M:
        
        if stack and stack[-1] == '(' and j == ')':
            stack.pop()
        else:
            stack.append(j)
    
    if len(stack):
        print('NO')
    else:
        print('YES')

        