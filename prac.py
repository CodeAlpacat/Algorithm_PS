# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
# import sys
from collections import deque
# input = sys.stdin.readline



#8 => 4  4 2//N
#6 0
#1 0
#4 0
#7 2
#0 5
#0 8
#0 3

#0은 그대로
#1은 하나만 겹치게
#2는 두개가 겹치게

T = int(input())

def recur(cur):

    

    for i in range(N//2):
        
        new_arr = []
        left_deck.extend([0] * i)
        recur(cur + 1)
        for j in range(len(right_deck)):
            if right_deck[j] != 0:
                new_arr.append(right_deck[j])
        
    


for tc in range(1, T+1):
    N = int(input())
    mat = list(map(int, input().split()))
    left_deck = mat[:2//len(mat)]
    right_deck = mat[2//len(mat):]
    