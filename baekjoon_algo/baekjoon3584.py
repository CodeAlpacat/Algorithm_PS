T = int(input())

for tc in range(T):
    N = int(input())
    par = [0 for _ in range(N+1)]
    for i in range(N-1):
        A, B = map(int, input().split())
        par[B] = A #b의 부모는 a이다

    x, y = map(int, input().split())

    arr_1 = [x]
    while par[x]:
        arr_1.append(par[x]) #부모를 찾는 경로를 저장 / 순서에 주의! 자기자신을 넣을지 말지.
        x = par[x] #x의 부모를 찾고 부모를 저장해 계속 부모를 찾아감.

    arr_2 = [y]
    while par[y]:
        arr_2.append(par[y])
        y = par[y]

    idx_1 = len(arr_1)-1
    idx_2 = len(arr_2)-1

    while idx_1 >= 0 and idx_2 >= 0 and arr_1[idx_1] == arr_2[idx_2]:
        idx_1 -= 1
        idx_2 -= 1
    print(arr_1[idx_1+1])