T = int(input())

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b, distance):
    a = find(a)
    b = find(b)
    
    if a == b:
        return 0
    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        par[a] = b
        rnk[b] += 1
    
    return distance

for tc in range(1, T+1):
    N = int(input())
    par = [i for i in range(N+1)]
    rnk = [0] * (N+1)

    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    
    E = float(input())
    edges = []
    for i in range(N):
        for j in range(i, N):
            distance = ((x_li[i] - x_li[j]) ** 2 + (y_li[i] - y_li[j]) ** 2) * E
            edges.append((distance, i, j))
    
    edges.sort()
    
    ans = 0 
    for i in edges:
        a = union(i[1], i[2], i[0])
        ans += a
    print(f'#{tc} {round(ans)}')