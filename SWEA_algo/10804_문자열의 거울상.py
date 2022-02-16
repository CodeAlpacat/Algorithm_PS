T = int(input())

arr = ['b', 'd', 'p', 'q']

for x in range(T):
    N = list(input())
    for i in range(len(N)):
        if N[i] == 'b':
            N[i] = 'd'
        
        elif N[i] == 'd':
            N[i] = 'b'

        elif N[i] == 'p':
            N[i] = 'q'

        else:
            N[i] = 'p'

    str_N = ''.join(N[::-1])

    print(f'#{x+1} {str_N}')