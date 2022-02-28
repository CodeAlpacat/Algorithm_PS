T = int(input())

for tc in range(T):
    li = [0] * 1002
    N = int(input())
    for i in range(N):
        bus_num, A, B = map(int, input().split())
        
        if bus_num == 1:
            for j in range(A+1, B):
                li[j] += 1
        
        if bus_num == 2:
            for j in range(A, B+1, 2):
                li[j] += 1
            if B % 2 == 1 and A % 2 == 0:
                li[B] += 1
            if B % 2 == 0 and A % 2 == 1:
                li[B] += 1
              

        if bus_num == 3:
            li[A] += 1                
            li[B] += 1
            if A % 2 == 0:
                for j in range(A+1, B):
                    if j % 4 == 0:
                        li[j] += 1
                    
            elif A % 2 == 1:
                for j in range(A+1, B):
                    if j % 3 == 0 and j % 10 != 10:
                        li[j] += 1        
    
    print(f'#{tc+1} {max(li)}')

#2 3 4 
#3 5 7 9
#4 8