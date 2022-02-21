#스텍 제로

def push(item, size):
    global top
    top += 1
    if top == size:
        return 'overflow'
    
    else:
        stack_li[top] = item
        
def pop():
    global top
    if top == -1:
        return 'underflow'
    else:
        top -= 1
        return stack_li[top+1]
        

T = int(input())

for x in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    stack_li = [0] * N

    top  = -1
    
    for i in range(len(li)):
        if li[i] != 0:
            push(li[i], N)
        else:
            pop()
    
    print(f'#{x+1} {stack_li[top]}')