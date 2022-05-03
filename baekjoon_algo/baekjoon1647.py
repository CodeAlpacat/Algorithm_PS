import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())

par = [i for i in range(N+1)]
rnk = [0] * (N+1)
mat = [list(map(int, input().split())) for _ in range(M)]
mat.sort(key=lambda x: x[2])

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return 
    
    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        par[a] = b
        rnk[b] += 1

ans = 0
for i in range(M):
    a, b = mat[i][0], mat[i][1]
    
    if find(a) == find(b):
        continue
    
    union(a, b)
    ans += mat[i][2]
    last_house_idx = i

print(ans - mat[last_house_idx][2])