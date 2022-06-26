from collections import deque
import math
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq
input = sys.stdin.readline
# 처음 시간초과 풀이
# def check(N):
#     cnt = 0
#     for i in range(1, N+1):
#         if i * i > N:
#             break
        
#         if N % i == 0:
#             cnt += i
#             if i * i != N:
#                 cnt += N // i
#     return cnt
        

# T = int(input())

# for tc in range(T):
#     n = int(input())
#     ans = 0
#     for i in range(1, n+1):
#         ans += check(i)
    
#     print(ans)



INF = 1000000
memo = [0 for _ in range(INF+1)]    
def get_dp():
    for i in range(1, INF+1):
        for j in range(i, INF+1, i):
            memo[j] += i #i의 배수들은 무조건 i를 약수로 가지므로 모두 미리 포함시키기
        memo[i] += memo[i-1] # 1~10까지의 누적합 적용

get_dp()
T = int(input())
for tc in range(T):
    n = int(input())
    print(memo[n])
    
# 1 2 3 4 5 6 7 8 9 10 / 10의 약수
# 1은 계속 반복, 2로 나누어 떨어지면 무조건 2를 약수로 가짐. (다시 계산X) => 메모이제이션 적용
# 1
# 1 2
# 1 3
# 1 2 4
# 1 5
# 1 2 3 6
# 1 7
# 1 2 4 8
# 1 3 9
# 1 2 5 10