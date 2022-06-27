# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

input = sys.stdin.readline

#1 2 3 4 5 6 7
#N = 100
#2 * 50 = 100
#4 * 25 = 100
#5 * 20 = 100

N = int(input())
cnt = 0
for i in range(2, N+1):
    if i * i > N:
        break

    if N % i == 0:
        cnt += 1

if N == 1:
    print("소수가 아닙니다")
elif cnt == 1:
    print("소수")
else:
    print('소수 아님')

