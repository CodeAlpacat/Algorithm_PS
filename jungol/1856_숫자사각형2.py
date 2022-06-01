n, m = map(int, input().split())
for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(m):
            print((i-1)*m+j+1, end=' ')
        print()
    else:
        for j in range(m, 0, -1):
            print((i-1)*m+j, end=' ')
        print()