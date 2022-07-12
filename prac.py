# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

# input = sys.stdin.readline
tc = 0
flag = False
res = []
while tc < 102:
    ans = []
    new_str = input()
    if new_str == '*':
        break
    if len(new_str) == 1:
        print(f'{new_str} is surprising.')
        continue

    for distance in range(len(new_str) - 2): #D 넘버
        for i in range(len(new_str)):
            for j in range(i, len(new_str)):
                if i == j:
                    continue

                if j-i-1 == distance:
                    ans.append(new_str[i] + new_str[j]+str(j-i-1))

    if len(ans) == len(set(ans)):
        print(f'{new_str} is surprising.')
    else:
        print(f'{new_str} is NOT surprising.')

    tc += 1
