def sosu(n):
    isPrime = [True for i in range(n + 1)]
    list_result = []

    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, n + 1):
        if not isPrime[i]:
            continue

        for j in range(i * i, n + 1, i):
            isPrime[j] = False
    
    for i in range(len(isPrime)):
        if isPrime[i]:
            list_result.append(i)
    return list_result

x, n = map(int, input().split())
a, b = sosu(x), [0] + sosu(n)

for i in range(len(a), len(b)):
    if x <= b[i] <= n:
        print(b[i])
    # 2 3 5 7 / 2 3 5 7 11 13 17 19