T = int(input())

def preorder(v):
    global cnt
    if v == 0: return
    cnt += 1
    preorder(L[v])
    preorder(R[v])

for tc in range(1, T+1):
    E, N = map(int, input().split())
    li = list(map(int, input().split()))
    L = [0] * (E+2)
    R = [0] * (E+2)

    for i in range(0, len(li), 2):
        if L[li[i]] != 0:
            R[li[i]] = li[i+1]
        else:
            L[li[i]] = li[i+1]
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')




def tree(cur, prv):
    sz[cur] = 1

    for nxt in graph[cur]:
        if nxt == prv:
            continue
        sz[cur] += tree(nxt, cur)

    return sz[cur]

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    graph = [[] for _ in range(E+2)]
    sz = [0] * (E+2)
    li = list(map(int, input().split()))

    for i in range(0, len(li), 2):
        graph[li[i]].append(li[i+1])

    tree(N, -1)


    print(f'#{tc} {sz[N]}')