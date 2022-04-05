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
    
    if rnk[a] < rnk[b]: # 크기가 큰쪽으로 붙게 만드는 식 (트리의 깊이가 변하지 않음.)
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else: # 같은 경우엔 루트의 레벨이 1만 늘어남.
        par[a] = b
        rnk[b] += 1


for tc in range(1, T+1):
    V, E = map(int, input().split())
    par = [i for i in range(V+1)]
    rnk = [0 for _ in range(V+1)]
    li = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        li.append((w, n1, n2))
    
    li.sort()
    w_min = 0
    for i in li:
        if find(i[1]) != find(i[2]):
            union(i[1], i[2])
            w_min += i[0]

    print(f'#{tc} {w_min}')
        