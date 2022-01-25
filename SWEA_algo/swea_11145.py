#사칙연산
from this import d


T = int(input())

def calculator(a, b, x):
    if x == '+':
        return a+b
    elif x == '-':
        return a-b
    elif x == '*':
        return a*b
    elif x == '/':
        return a//b
    else:
        return


i = 1
for _ in range(T):
    N, M, X= input().split()
    
    print(f'#{i}', calculator(int(N), int(M), X))
    i += 1
