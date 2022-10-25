# sys.stdin=open('sample_input.txt')
# import collections
import heapq
import math
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
prefix = [[[0] * 10 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, 10):
            if k == arr[i][j]:
                prefix[i][j][k] += 1
            prefix[i][j][k] += prefix[i-1][j][k] + prefix[i][j-1][k] - prefix[i-1][j-1][k]

Q = int(input())

for i in range(Q):
    a, b, c, d =  map(int, input().split())
    ans = 0
    for k in range(1, 10):
        if prefix[c][d][k] - prefix[c][b - 1][k] - prefix[a-1][d][k] + prefix[a-1][b-1][k]:
            ans += 1

    print(ans)