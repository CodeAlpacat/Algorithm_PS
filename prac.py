# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
from platform import node
import sys
from collections import deque

input = sys.stdin.readline

#에라토스테네스로 거른다
#거른 소수들의 조합이 N이 되는 경우를 구한다.

N = int(input())

prime_list = [True for _ in range(N+1)]
prime_list[0], prime_list[1] = False, False

for i in range(2, len(prime_list)):
    
    for j in range(i*i, N+1, i):
        if prime_list[j]:
            prime_list[j] = False

prime_mat = []
for i in range(len(prime_list)):
    if prime_list[i]:
        prime_mat.append(i)

prime_mat = prime_mat + [0]
s = 0
e = 0
total = prime_mat[0]
cnt = 0
while e < len(prime_mat)-1:
    
    if total < N:
        e += 1
        total += prime_mat[e]
    elif total > N:
        total -= prime_mat[s]
        s += 1
    else:
        cnt += 1
        e += 1
        total += prime_mat[e]

print(*prime_mat)
print(cnt)


