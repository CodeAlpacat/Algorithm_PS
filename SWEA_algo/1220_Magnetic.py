
for t in range(10):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
    
    
    res = 0

    for i in range(100):
        cross = False
        for j in range(100):
            if li[j][i] == 0:
                continue
            elif li[j][i] == 1:
                cross = True
            elif li[j][i] == 2 and cross:
                res += 1
                cross = False
    
    print(f'#{t+1} {res}')