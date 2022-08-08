N = int(input())

for i in range(N):
    stack = []
    
    M = input()
    for j in M:
        
        if stack and stack[-1] == '(' and j == ')':
            stack.pop()
        else:
            stack.append(j)
    
    if len(stack):
        print('NO')
    else:
        print('YES')