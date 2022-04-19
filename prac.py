from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

print(pow(A, B, C))