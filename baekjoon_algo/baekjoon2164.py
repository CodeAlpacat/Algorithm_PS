# import sys
from collections import deque
# input = sys.stdin.readline

N = int(input())

mat = [i for i in range(1, N+1)]
q = deque(mat)
while len(mat) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])