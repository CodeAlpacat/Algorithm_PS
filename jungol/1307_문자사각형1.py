n = int(input())

for i in range(n, 0, -1):
    for j in range(1, n+1):
        cnt = n*n-1 + i - n*j
        cnt %= 26
        print(chr(65+ cnt), end=' ')
    print()