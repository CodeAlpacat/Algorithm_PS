# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.extend(list(map(int, input().split())))

print(*sorted(A))