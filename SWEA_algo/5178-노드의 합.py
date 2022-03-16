T = int(input())


def post_order(v):
    global li
    if v > N + 1: return 0
    
    if li[v] > 0: #노드가 0이어야 더해서 넣어줌.
        return li[v]
    
    L, R = v * 2, v * 2 + 1

    li[v] = post_order(L) + post_order(R)
    return li[v]
for tc in range(T):
    N, M, L = map(int, input().split())
    li = [0] * (N+2)

    for i in range(M):
        node, value = map(int, input().split())
        li[node] = value
    
    ans = post_order(L)
    print(f'#{tc+1} {ans}')
