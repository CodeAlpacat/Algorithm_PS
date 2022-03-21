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
memo[0] = [0 for _ in range(K+1)]
item_list = [[]]
for _ in range(N):
    item_list.append(list(map(int, input().split())))
print(dp(N, K))

print(memo)