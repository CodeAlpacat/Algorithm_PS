# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
woods = list(map(int, input().split()))
s, e = 1, max(woods)

while s <= e:
    m = (s+e) // 2

    a = 0
    for i in woods:
        if i >= m:
            a += i - m
    if a >= M:
        s = m + 1
    else:
        e = m - 1
print(e)