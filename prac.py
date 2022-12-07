# sys.stdin=open('sample_input.txt')
import heapq
import math
import sys
from collections import deque

# input = sys.stdin.readline

n = input()

n_len = len(n) - 1

answer = 0

for i in range(n_len):
    answer += 9 * (10 ** i) * (i + 1)

answer += ((int(n) - (10 ** n_len)) + 1) * (n_len + 1)

print(answer)