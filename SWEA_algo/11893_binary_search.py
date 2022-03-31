def binary_search(N):
    s = 0
    e = len(A)-1
    flag = 0
    while s <= e:
        m = (s + e) // 2
        if A[m] == N:
            return 1

        elif A[m] > N:
            e = m - 1
            if flag == 1:
                return 0
            flag = 1
        else:
            s = m + 1
            if flag == -1:
                return 0
            flag = -1

    return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(len(B)):
        if binary_search(B[i]):
            cnt += 1

    print(f'#{tc} {cnt}')