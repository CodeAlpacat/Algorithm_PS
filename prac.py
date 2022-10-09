# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break
    if n == m + 1:
        print("There is one tree.")
    for i in range(n):
        a, b = map(int, input().split())
