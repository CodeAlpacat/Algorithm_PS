import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
v = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)

sz = [0] * (N+1)
def dfs(cur, prv):
    sz[cur] = 1
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        sz[cur] += dfs(nxt, cur)
    return sz[cur]


dfs(R, -1)

arr = []
for i in range(Q):
    U = int(input())
    arr.append(sz[U])

for i in arr:
    print(i)