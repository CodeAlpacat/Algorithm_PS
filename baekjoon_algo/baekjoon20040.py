N, M = map(int, input().split())

par = [i for i in range(N+1)]
rnk = [0 for _ in range(N+1)]

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
        rnk[a] += 1
        par[b] = a
save = []
for i in range(M):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i+1)
        break
else:
    print(0)