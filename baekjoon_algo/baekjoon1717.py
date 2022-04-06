N, M = map(int, input().split())
import sys
input = sys.stdin.readline
par = [i for i in range(N+1)]
rnk = [0] * (N+1)

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        rnk[b] += 1
        par[a] = b

for i in range(M):
    a, b, c = map(int, input().split())

    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')


##############################


import sys
input = sys.stdin.readline
N, M = map(int, input().split())

par = [-1 for i in range(N+1)]

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if par[a] < par[b]:
        par[b] = a
    elif par[b] < par[a]:
        par[a] = b
    else:
        par[a] -= 1
        par[b] = a

for i in range(M):
    a, b, c = map(int, input().split())

    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')