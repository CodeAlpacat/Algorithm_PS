# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline

N = int(input())
mat = set(map(int, input().split()))
print(*sorted(list((mat))))
