def same(n):
    if len(n) == 1 or len(n) == 0:
        return True
    
    if n[0] == n[-1]:
        return same(n[1:len(n)-1])
T = int(input())

result_list = []
for x in range(T):
    N, M  =map(int, input().split())
    M_li = []

    for i in range(N):
            line = list(input())
            M_li.append(line)
    
    for i in range(N):
        for j in range(N-M+1): #첫 줄 0번 케이스 8개 인덱스 7에서 20까지
            ans = ''
            ans_col = ''
            for k in range(j, j+M):
                ans += M_li[i][k]
                ans_col += M_li[k][i]
            if same(ans): # M길이의 문자열인가
                result_list.append(ans)

            if same(ans_col):
                result_list.append(ans_col)

for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')
    