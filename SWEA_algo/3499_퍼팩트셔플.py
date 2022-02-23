T = int(input())

for t in range(T):
    N = int(input())
    li = list(input().split())
    
    if N % 2 == 0:
        print(f'#{t+1}', end = ' ')
        for i in range(N//2):
            print(li[i], end = ' ')
            print(li[i +(N//2)], end = ' ')
        print()
    if N % 2 == 1:
        print(f'#{t+1}', end = ' ')
        for i in range(N//2):
            print(li[i], end =' ')
            print(li[i+(N//2 + 1)], end = ' ')
        print(li[N//2], end = ' ')
        print()