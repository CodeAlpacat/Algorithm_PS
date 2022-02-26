#수 이어가기
N = int(input())

li_res = []
cnt_max = -10000000
for i in range(0, N+1):
    li = [N]
    li.append(i)
    cnt = 0
    start = 1
    while True:
        if li[start - 1] - li[start] < 0:
            break
        else:
            cnt += 1
            li.append(li[start - 1] - li[start])
        start += 1

    if len(li) > cnt_max:
        li_res = []
        for j in li:
            li_res.append(j)
        cnt_max = len(li)

print(cnt_max)
print(*li_res)