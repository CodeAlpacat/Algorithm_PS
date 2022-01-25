#배수 출력
T = int(input())

for x in range(T):
    N, M = map(int, input().split())
    i = 1
    print(f'#{x+1}', end =' ')
    while True:
        if N*i > M:
            break
        print(N*i, end = ' ')
        i += 1
    print()
    
