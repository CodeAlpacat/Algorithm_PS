import math
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    print("0.00")
    exit()
par = [i for i in range(N+1)]
rnk = [0 for _ in range(N+1)]
node = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

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
    elif rnk[b] < rnk[a]:
        par[b] = a
    else:
        par[a] = b
        rnk[b] += 1



#원래 있던 길은 이어줌
for i in range(M):
    u, v = map(int, input().split())
    if find_(u) != find_(v):
        union_(u, v)

mst_list = []

for i in range(1, N):
    for j in range(i+1, N+1):
        mst_list.append([i, j, math.sqrt((node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2)])

mst_list.sort(key=lambda x: x[2])

ans = 0
for i in range(len(mst_list)):
    a, b, dist = mst_list[i][0], mst_list[i][1], mst_list[i][2],
    
    if find_(a) != find_(b):
        union_(a, b)
        ans += dist

print(format(ans, ".2f"))