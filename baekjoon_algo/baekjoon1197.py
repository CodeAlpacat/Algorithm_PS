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

n, m = map(int, input().split())
v = [list(map(int, input().split())) for i in range(m)]
par = [i for i in range(n+1)] #정점의 노드
rnk = [0 for i in range(n+1)] #트리의 레벨

v.sort(key=lambda x:x[2])


ans = 0
for i in range(m):
    x, y = v[i][0], v[i][1]

    if find(x) == find(y):
        continue

    union(x, y)
    ans += v[i][2]
print(*par)
print(ans)