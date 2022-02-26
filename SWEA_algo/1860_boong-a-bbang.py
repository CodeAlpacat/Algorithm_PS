T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split()) # 손님수, M초 동안 K개 붕어빵
    li = list(map(int, input().split())) # 손님이 도착하는 시간
    li.sort()
    cnt = 0
    fish_num = 0 # 붕어빵 개수
    sec = 0 # 현재 시간
    bool_stop = True
    while True:
        if li[-1] < sec:
            print(f'#{tc+1} Possible')
            break
        if sec != 0 and sec % M == 0:
            fish_num += K

        for i in li:
            if i == sec:
                if fish_num <= 0:
                    print(f'#{tc+1} Impossible')
                    bool_stop = False
                    break
                fish_num -= 1
        if not bool_stop:
            break

        sec += 1