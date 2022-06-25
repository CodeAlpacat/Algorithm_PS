#에라토스테네스의 체
#K가 주어지면  K에 가장 근접한 두 소수를 찾는다.
T = int(input())

mat = [1 for _ in range(1300000)]
for i in range(2, len(mat)):
    
    for j in range(i*i, len(mat), i):
        mat[j] = False


for tc in range(T):
    k = int(input())
        
    ans = 0xffffff
    prev = 0
    nxt = 0
    if mat[k]: #2 3 5 7 11
        print(0)
    else:
        for i in range(2, len(mat)):
            if k > i and mat[i]:
                prev = i
            
            if k < i and mat[i]:
                nxt = i
                ans = nxt - prev
                break
        
                
        print(ans)        
    
