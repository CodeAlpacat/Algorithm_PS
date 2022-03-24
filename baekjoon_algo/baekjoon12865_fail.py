#평범한 배낭
from sys import stdin
input = stdin.readline

def recur(n, w):
    
    if n == 0 or w == 0:
        return memo[n][w]
    
    if item_list[n][0] > w:
        memo[n][w] = recur(n-1, w)
        return memo[n][w]

    if memo[n][w] != -1:
        return memo[n][w]
    
    memo[n][w] = max(recur(n-1, w - item_list[n][0]) + item_list[n][1], recur(n - 1, w))
    return memo[n][w]

N, K = map(int, input().split())
item_list = [[0, 0]]
for i in range(1, N+1):
    item_list.append(list(map(int, input().split())))
memo = [[0] + [-1] * K for _ in range(N+1)]
memo[0] = [0] * (K+1)
print(recur(N, K))



#평범한 배낭

def recur(cur, w_total, v_total):
    global ans
    if w_total > K:
        return
    
    if w_total <= K:
        ans = max(ans, v_total)

    if cur == N:
        return


    recur(cur + 1, w_total + item_list[cur][0], v_total + item_list[cur][1])
    recur(cur + 1, w_total, v_total)



N, K = map(int, input().split())
item_list = [[] for _ in range(N)]
for i in range(N):
    W, V = map(int, input().split())
    item_list[i].append(W)
    item_list[i].append(V)


ans = 0
recur(0, 0, 0)

print(ans)



###############
import sys
input = sys.stdin.readline

def dp(n, w):
    global memo,item_list
    if  w<0:
        return -100000000
    if memo[n][w] != -1:
        return memo[n][w]

    memo[n][w] = max(dp(n-1, w-item_list[n][0]) + item_list[n][1], dp(n-1, w))
    return memo[n][w]
    
N, K = map(int, input().split())
memo = [[0]+[-1 for _ in range(K)] for _ in range(N+1)]
memo[0] = [-1 for _ in range(K+1)]
item_list = [[]]
for _ in range(N):
    item_list.append(list(map(int, input().split())))
print(dp(N, K))