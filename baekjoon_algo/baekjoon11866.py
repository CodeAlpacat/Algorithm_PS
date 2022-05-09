from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

#1, 2, 3, 4, 5, 6, 7
#peak이 1씩 증가 => popleft한 값들을 q다시 append해서 저장
#3, 4, 5, 6, 7, 1, 2
#3이면 popleft()을 mat 리스트에 추가

input = sys.stdin.readline
N, K = map(int, input().split())

peak = 1

q = deque([i for i in range(1, N+1)])

ans = []
while q:
    if peak < K:
        q.append(q.popleft())
        peak += 1
    elif peak == K:
        ans.append(q.popleft())
        peak = 1

print('<', end='')
for i in range(len(ans)):
    print(ans[i], end='')
    if i == len(ans)-1:
        break
    print(', ', end='')  
print('>')