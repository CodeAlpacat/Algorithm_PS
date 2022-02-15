T = int(input())

def binary(p, num):
    cnt = 1
    s = 1
    e = p
    while s <= e:
        m = (s + e) // 2
        if m == num:
            return cnt
        elif m < num:  # A가 중간지점보다 큰 경우
            s = m
            cnt += 1
        elif m > num:  # A가 중간보다 작은 경우
            e = m
            cnt += 1


for x in range(T):
    P, A, B = map(int, input().split())
    A_bi = binary(P, A)
    B_bi = binary(P, B)
    result = ''
    if A_bi < B_bi:
        result = 'A'
    elif A_bi > B_bi:
        result = 'B'
    else:
        result = 0

    print(f'#{x + 1} {result}')
