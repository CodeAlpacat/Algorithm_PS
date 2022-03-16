def inorder(v):
    if v == 0: return

    inorder(L[v])
    print(P[v], end ='')
    inorder(R[v])


for tc in range(1, 11):
    N = int(input())
    L = [0] * (N+1)
    R = [0] * (N+1)
    P = [0]  * (N+1)
    
    for i in range(N):
        li = [0] * 4
        node = list(input().split())
        for i in range(len(node)):
            if node[i].isdigit():
                node[i] = int(node[i])
        
        for i in range(len(node)):
            li[i] = node[i]
        
        L[node[0]] = li[2]
        P[node[0]] = li[1]
        R[node[0]] = li[3]
    print(f'#{tc}', end =' ')
    inorder(1)
    print()

# def inorder(v):
#     global V
#     L, R = v * 2, v * 2 + 1
#     if L <= V:
#         inorder(L)
#     print(tree[v], end='')
#     if R <= V:
#         inorder(R)
 
 
# for tc in range(1, 11):
#     V = int(input())
#     tree = [0] * (V + 1)
#     for _ in range(V):
#         info = input().split()
#         tree[int(info[0])] = info[1]
 
#     print(f'#{tc}', end=' ')
#     inorder(1)
#     print()