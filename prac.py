from collections import deque
import math
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq


N = int(input())
ans = []
X = N

for i in range(2, N+1):
    if i * i > N:
        break
    
    while X % i == 0:
        ans.append(i)
        X //= i

for i in ans:
    print(i)
if X != 1:
    print(X)
else:
    pass