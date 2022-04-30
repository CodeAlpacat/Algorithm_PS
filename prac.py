from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

def recur(cur, total):
    global ans
    if cur == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if visited[i]:
            continue

        copy_price = [0] * N
        for k in range(N):
            copy_price[k] = coin_price[k]

        for j in range(N):
            coin_price[j] -= list_discount[i][j]
            if coin_price[j] < 1:
                coin_price[j] = 1
        
        visited[i] = True
        recur(cur+1, total + coin_price[i])
        visited[i] = False

        for k in range(N):
            coin_price[k] = copy_price[k]



N = int(input())
coin_price = list(map(int, input().split()))

list_discount = [[0]*N for _ in range(N)]
visited = [False] * N

for i in range(N):
    T = int(input())
    for j in range(T):
        a, b = map(int, input().split())
        list_discount[i][a-1] = b

ans = 0xffffff
recur(0, 0)
print(ans)