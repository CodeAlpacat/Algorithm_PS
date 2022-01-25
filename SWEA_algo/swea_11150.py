#별찍기2
T = int(input())

for i in range(T):
    N = int(input())
    print(f'#{i+1}')
    for j in range(1, N+1): # N*N 줄
        for k in range(1, j+1):
            print('*', end ='')
        print()