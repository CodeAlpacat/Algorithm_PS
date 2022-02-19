T = int(input())

for x in range(T):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    li_cnt = [[0] * N for _ in range(N)]
    sum_res = 0
    for i in range(M):
        sx, sy, s_len = map(int, input().split())

        for j in range(sx, s_len + sx):
            for k in range(sy, s_len + sy):
                if k < N and j < N:
                    li_cnt[j][k] += 1
                else:
                    continue

    for i in range(len(li)):
        for j in range(len(li)):
            if li_cnt[i][j] >= 1:
                sum_res += li[i][j]

    print(f'#{x+1} {sum_res}')