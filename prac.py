T = int(input())

def enque(n): #최소힙
    tree.append(n)
    p = len(tree) - 1
    while p > 1 and tree[p//2] > tree[p]:
        tree[p], tree[p//2] = tree[p//2], tree[p]
        p = p // 2

for tc in range(1, T+1):
    N = int(input())
    heap = list(map(int, input().split()))
    tree = [0]
    for i in heap:
        enque(i)

    total = 0
    idx = N // 2
    while idx:
        total += tree[idx]
        idx //= 2
    
    print(f'#{tc} {total}')

