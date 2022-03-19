T = int(input())
def inorder(v):
    global cnt
    if v == 0:
        return
    L = v * 2
    R = v * 2 + 1
    if L < N+1:
        inorder(L)
    tree[v] = cnt
    cnt += 1
    if R < N+1:
        inorder(R)

for tc in range(1, T+1):
    N = int(input())
    tree = [i for i in range(N+1)]
    
    cnt = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')