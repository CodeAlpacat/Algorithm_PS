from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq



T = int(input()) #T는 케이스 개수 3


for tc in range(1, T+1): #테스트 케이스 for 문 3번
    input_list = list(map(int, input().split())) #인풋 받아서 리스트로 만들어줌
    
    answer = 0
    #평균 값구하는 수만큼 반복
    for i in range(len(input_list)):
        answer += input_list[i]
    
    answer /= len(input_list) #float 자료형
    if answer == int(answer): #소수점이 존재하면 int로 바꾼값하고 다르니까 그
        print(f'#{tc} {int(answer)}')
    else:
        print(f'#{tc} {int(answer)+1}')
