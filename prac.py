# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline


a, b = input().split()

result = []
for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            cnt += 1
    result.append(cnt)

print(min(result))