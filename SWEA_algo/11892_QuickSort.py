
def quick_sort(s, e):
    if s >= e: return
    # 파티션

    i, j = s, e
    while i < j:
        while i <= e and arr[s] >= arr[i]:
            i += 1
        while arr[s] < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    quick_sort(s, j - 1)
    quick_sort(j + 1, e)

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print(f'#{tc} {arr[N//2]}')