import sys
N = int(sys.stdin.readline())
par = [i for i in range(1000010)]
rnk = [0 for i in range(1000010)]
sz = [1 for i in range(1000010)]

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
        sz[b] += sz[a]
    elif rnk[a] > rnk[b]:
        par[b] = a
        sz[a] += sz[b]
    else:
        rnk[a] += 1
        par[b] = a
        sz[a] += sz[b]


for i in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'I':
        union_(int(order[1]), int(order[2]))
    
    elif order[0] == 'Q':
        print(sz[find_(int(order[1]))])
