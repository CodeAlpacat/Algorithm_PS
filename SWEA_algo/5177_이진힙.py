T = int(input())

def enque(n): #최소힙
    global top
    top += 1
    tree[top] = n
    c = top
    p = c//2
    while p > 0 and tree[p] > tree[c]: #부등호 방향이 최소 최대 힙 결정
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

for tc in range(1, T+1):
    N = int(input())
    heap = list(map(int, input().split()))
    top = 0
    tree = [0] * 1000000
    arr = [0]
    for i in heap:
        enque(i)

    total = 0
    idx = N // 2
    while idx:
        total += tree[idx]
        idx //= 2
    
    print(f'#{tc} {total}')


# T = int(input())

# def enque(n): #최소힙
#     tree.append(n)
#     p = len(tree) - 1
#     while p > 1 and tree[p//2] > tree[p]:
#         tree[p], tree[p//2] = tree[p//2], tree[p]
#         p = p // 2

# for tc in range(1, T+1):
#     N = int(input())
#     heap = list(map(int, input().split()))
#     tree = [0]
#     for i in heap:
#         enque(i)

#     total = 0
#     idx = N // 2
#     while idx:
#         total += tree[idx]
#         idx //= 2
    
#     print(f'#{tc} {total}')