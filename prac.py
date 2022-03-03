T = int(input())
for tc in range(T):
    N = int(input()) #N 시간중에  ai 번 잠듬. 최대 1000000
    li = list(map(int, input().split()))
    max_num = max(li)
    new_li = []
    for i in range(1, len(li)):
        if li[i] + li[i-1] == max_num:
            new_li.append(li[i] + li[i-1])
        elif li[i] == max_num:
            new_li.append(li[i])
        elif li[i] + li[i-1] > max_num:
            continue
        