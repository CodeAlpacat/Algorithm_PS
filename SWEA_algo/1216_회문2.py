def same(n):
    if len(n) == 1 or len(n) == 0:
        return True
    
    if n[0] == n[-1]:
        return same(n[1:len(n)-1])

for x in range(10):
    N = int(input())
    li = [list(input()) for i in range(100)]
    li_2 = []
    
    for i in range(100):
        str_n = ''
        for j in range(100):
            str_n += li[j][i] #재사용을 위한 새로축을 가로축으로 표현
        li_2.append(str_n)
        
    res = 0
    for i in range(100, 0, -1):
        if res >= i:
            break
        for j in range(100):
            if res == i:
                break
            # 0부터 가장 긴 회문을 찾고 길이 -1 씩해서 회문을 찾으면 스탑 => 최장길이
            for k in range(100-i+1): 
                if same(li[j][k:k+i]) or same(li_2[j][k:k+i]):
                    res = i
                    break
        
        
    print(f'#{x+1} {res}')