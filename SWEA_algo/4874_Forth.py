T = int(input())
for t in range(T):
    li = list(input().split())
    postfix = []
    for i in li:
        if i.isdigit():
            postfix.append(i)
        elif i == '+' and len(postfix)>1:
            a = int(postfix.pop())
            b = int(postfix.pop())
            postfix.append(b + a)
        elif i == '*' and len(postfix)>1:
            a = int(postfix.pop())
            b = int(postfix.pop())
            postfix.append(b * a)
        elif i == '/' and len(postfix)>1:
            a = int(postfix.pop())
            b = int(postfix.pop())
            postfix.append(b // a)
        elif i == '-' and len(postfix)>1:
            a = int(postfix.pop())
            b = int(postfix.pop())
            postfix.append(b - a)
        elif i == '.' and len(postfix) == 1:
            print(f'#{t+1} {postfix[0]}')
        else:
            print(f'#{t+1} error')
            break