T = int(input())

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

for tc in range(1, T+1):
    N, M = map(int, input().split())
    par = [i for i in range(N+1)]
    rnk = [0] * (N+1)
    
    for i in range(M):
        a, b = map(int, input().split())
        union(a, b)
    cnt = 0
    for i in range(1, N+1):
        if par[i] == i:
            cnt += 1

    print(f'#{tc} {cnt}')