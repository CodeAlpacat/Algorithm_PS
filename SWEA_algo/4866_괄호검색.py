T = int(input())

def check(n):
    global peak_li
    for i in n:
        if i == '(' or i == '{':
            li.append(i)
            
        elif i == ')' or i == '}':
            if len(li) == 0: # )이 나오면 맨 끝이 ( 이어야함.
                peak_li = 0
                break
                
            elif i == ')' and li.pop() == '{':
                peak_li = 0
                break
            
            elif i == '}' and li.pop() == '(':
                peak_li = 0
                break
    if len(li):
        peak_li = 0

for x in range(T):
    N = input()
    li = []
    peak_li = 1
    check(N)
    
    print(f'#{x+1} {peak_li}')