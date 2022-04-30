import sys
input = sys.stdin.readline
def recur(cur, total):
    global ans
    if cur == N:
        ans = min(ans, total)
        return

    for i in range(N):
        if visited[i]:
            continue


        for j in range(N):
            coin_price[j] -= list_discount[i][j]
        
        origin = coin_price[i]
        if coin_price[i] < 1:
            coin_price[i] = 1
        
        visited[i] = True
        recur(cur+1, total + coin_price[i])
        visited[i] = False
        
        coin_price[i] = origin

        for j in range(N):
            coin_price[j] += list_discount[i][j]



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