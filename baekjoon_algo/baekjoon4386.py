import math
import sys
input = sys.stdin.readline

N = int(input())
node = [0] + [list(map(float, input().split())) for _ in range(N)]
par = [i for i in range(N+1)]
rnk = [0 for i in range(N+1)]

def find_(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_(par[x])
        return par[x]

def union_(a, b):
    a = find_(a)
    b = find_(b)

    if a == b:
        return 
    
    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        rnk[a] += 1
        par[b] = a

mat = []

for i in range(1, N+1):
    for j in range(i, N+1):
        if i != j:
            mat.append([i, j, math.sqrt((node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2)])

mat.sort(key=lambda x: x[2])

ans = 0
for i in range(len(mat)):
    u, v, dist = mat[i][0], mat[i][1], mat[i][2]
    
    if find_(u) != find_(v):
        union_(u, v)
        ans += dist

print(format(ans, ".2f"))