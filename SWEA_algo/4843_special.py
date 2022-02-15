def select(arr):
    for i in range(0, len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


T = int(input())

for x in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    a = select(li)

    new_li = []
    print(f'#{x+1}', end = ' ')
    for i in range(5):
        print(a[len(a)-i-1], end = ' ')
        print(a[i], end = ' ')
    print()
