# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
from collections import deque

#mobitel
#아스키 코드로 변환 => 정렬

#mob ite l 정렬

alpha = list(input())
ans = []
for i in range(1, len(alpha) - 1):
    for j in range(i + 1, len(alpha)):
        a = alpha[0:i]
        b = alpha[i:j]
        c = alpha[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ans.append(a + b + c)
for i in range(len(ans)):
    ans[i] = ''.join(ans[i])

print(sorted(ans)[0])