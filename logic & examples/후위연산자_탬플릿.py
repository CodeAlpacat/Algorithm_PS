#계산기3
for t in range(10):
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(':3}
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(':0}
    stack = []
    postfix = [] #+(+
    N = int(input())
    li = list(input()) #3 + (4+5)*6+7
    for i in li:#345+6*+7+
        if i in icp:
            while stack and isp[stack[-1]] >= icp[i]: #스택의 top의 기준으로 들어오는 기준이 작은 것들 전부 pop
                postfix.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(i) # 피연산자

    while stack: #남은연산자들 전부 postfix에 넣어주기
        postfix.append(stack.pop())

#계산은 반대로
    ans = 0
    for i in postfix:
        if i in icp:
            first = int(stack.pop())
            second = int(stack.pop())
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
    
    print(f'#{t+1} {stack[0]}')