# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys

def solution(n):
    answer = 1
    
    for i in range(1, n+1):
        total = 0
        for j in range(i, n+1):
            if total > n:
                break
                
            if total == n:
                answer += 1
                break
                
            total += j
        
    return answer