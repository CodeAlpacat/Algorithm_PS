# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys

X, Y = map(int, input().split())
Z = (Y * 100) // X
cnt = 0
l = 1
r = X
#처음부터 100이 아니면 아무리 높아도 99
if Z == 100 or Z == 99:
    print(-1)
else:
    while l <= r:
        m = (l + r) // 2
        if (Y + m) * 100  // (X + m) <= Z:
            l = m + 1
        else:
            cnt = m
            r = m - 1

    print(cnt)