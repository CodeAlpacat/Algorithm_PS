import sys
input = sys.stdin.readline

N = int(input())
par = [i for i in range(N+1)]
rnk = [0 for _ in range(N+1)]

def _find(x):
    if par[x] == x:
        return x
    else:
        par[x] = _find(par[x])
        return par[x]

def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a == b:
        return 
    
    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        rnk[a] += 1
        par[b] = a

planet_x = []
planet_y = []
planet_z = []
for i in range(1, N+1):
    x, y, z = map(int, input().split())
    planet_x.append([x, i])
    planet_y.append([y, i])
    planet_z.append([z, i])

planet_x.sort()
planet_y.sort()
planet_z.sort()

cnt_mat = []

for i in range(1, N):
    cnt_mat.append([abs(planet_x[i][0] - planet_x[i-1][0]), planet_x[i][1], planet_x[i-1][1]])
    cnt_mat.append([abs(planet_y[i][0] - planet_y[i-1][0]), planet_y[i][1], planet_y[i-1][1]])
    cnt_mat.append([abs(planet_z[i][0] - planet_z[i-1][0]), planet_z[i][1], planet_z[i-1][1]])

cnt_mat.sort()

ans = 0
cnt = 0
for i in cnt_mat:
    cost, a, b = i
    if _find(a) != _find(b):
        _union(a, b)
        ans += cost
        cnt += 1
    if cnt == N:
        break

print(ans)