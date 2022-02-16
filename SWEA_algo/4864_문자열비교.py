T = int(input())

for x in range(T):
    N = input()
    M = input()
    result = 0
    for i in range(len(M)-len(N)+1):
        if M[i:i+len(N)] == N:
            result = 1
            a = M[i:i+len(N)]
    

    print(f'#{x+1} {result}')