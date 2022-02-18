#쇠막대기
T = int(input())

for x in range(T):
    N = input()
    cnt = 1 # 시작은 무조건 '('
    ans = 0    
    for i in range(1, len(N)):
        if N[i] == '(':
            cnt += 1
        else:
            if N[i-1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    print(f'#{x+1} {ans}')