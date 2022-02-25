for t in range(10):
    N = int(input())
    li = list(map(int, input().split()))
    s = 0
    minus = 0
    while True:
        if li[s] - minus - 1 <= 0:
            li[s] = 0
            break
        li[s] -= (minus + 1)

        minus += 1
        s += 1
        minus = minus % 5
        s = s % len(li)
    s += 1
    print(f'#{N}', end =' ')
    for i in range(len(li)):
        print(li[s], end = ' ')
        s += 1
        s = s % len(li)
    print()

        
