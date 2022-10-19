import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
prefix = [0 for i in range(N+1)]

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i]

for _ in range(M):
    a, b = map(int, input().split())
    
    print(prefix[b] - prefix[a-1]) 