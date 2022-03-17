
def post_order(v):
    if v == 0:
        return
    post_order(L[v])
    post_order(R[v])
    ans_post_order.append(tree[v])

op = ['+', '-', '*', '/']
def post_calc(postfix):
    stack = []
    for i in postfix:
        if i in op:
            first = stack.pop()
            second = stack.pop()        
            if i == '+':
                stack.append(second + first)
            elif i == '-':
                stack.append(second - first)
            elif i == '*':
                stack.append(second * first)
            elif i == '/':
                stack.append(second / first)
            else:
                stack.pop()

        else:
            stack.append(i)
    return stack[0]
        
        
for tc in range(1, 11):
    N = int(input())
    L = [0] * (N+1)
    R = [0] * (N+1)
    tree = [0] * (N+1)
    for i in range(N):
        li_input = list(input().split())
        if li_input[1].isdigit():
            tree[int(li_input[0])] = int(li_input[1])
        
        else:
            tree[int(li_input[0])] = li_input[1]
            L[int(li_input[0])] = int(li_input[2])
            R[int(li_input[0])] = int(li_input[3])
    ans_post_order = []
    post_order(1)
    print(f'#{tc} {int(post_calc(ans_post_order))}')