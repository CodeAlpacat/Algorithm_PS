#큐_숫자카드
T = int(input())

for t in range(T):
    N = int(input())
    li = [i for i in range(1, N+1)]
    
    s = 0
    cnt = 0
    while len(li)-1 > s:
        if s % 2 == 0:
            s += 1
            li.append(li[s])
        else:
            s += 1
    
    print(f'#{t+1} {li[s]}')