import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]
prefix = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + arr[i][j]
    
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])