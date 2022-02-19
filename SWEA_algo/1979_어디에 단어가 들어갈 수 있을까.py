T = int(input())

for x in range(T):
    N, K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for i in range(N):
        cnt_r = 0 #가로
        cnt_c = 0 #세로
        for j in range(N):
            if li[i][j]:
                cnt_r += 1
            else:
                if cnt_r == K:
                    res += 1
                cnt_r = 0
            if j == N-1 and cnt_r == K:
                res += 1

            if li[j][i]:
                cnt_c += 1
            else:
                if cnt_c == K:
                    res += 1
                cnt_c = 0

            if j == N-1 and cnt_c == K:
                res += 1
    print(f'#{x+1} {res}')