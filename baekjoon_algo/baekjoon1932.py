import sys
input = sys.stdin.readline

N = int(input())

tri = [list(map(int, input().split())) for _ in range(N)]

def recur(x, y):
    if x > N:
        return -0xffffff
    
    if y == N:
        x += 1
        y = 0
    if x == N-1:
        return tri[0][0]
    if memo[x][y] != -1:
        return memo[x][y]
    
    memo[x][y] = max(recur(x+1, y) + tri[x+1][y], recur(x+1, y+1) +tri[x+1][y+1])
    return memo[x][y]
memo = [[-1] * N for _ in range(N)]
print(recur(0, 0))