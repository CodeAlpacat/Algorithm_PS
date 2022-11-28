# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

# '('가 추가되면 count += 1
# 누적으로 쌓이다가 ')'가 등장하면 '('를 제거하고 count만큼 result에 더함
mat = list(input())
stack = [mat.pop(0)]
result = 0
count = 1
while mat:
    if stack[-1] == '(':
        if mat[0] == ')':
            count -= 1
            result += count
        elif mat[0] == '(':
            count += 1

    elif stack[-1] == ')':
        if mat[0] == ')':
            count -= 1
            result += 1
        if mat[0] == '(':
            count += 1

    #(가 나왔을 때,
    stack.append(mat.pop(0))

print(result)