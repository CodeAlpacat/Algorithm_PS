set_li = set()
N, M, K = map(int, input().split())
li = []
total = 0
pick = 0
def recur(cur, cnt):
    global total, pick

    if cur == N:
        if cnt == M:
            count = 0
            total += 1
            for i in range(len(li)):
                if li[i] <= M:
                    count += 1
            if count >= K:
                pick += 1
        return

    li.append(cur+1)
    recur(cur + 1, cnt + 1)
    li.pop()

    recur(cur + 1, cnt)

recur(0, 0)
print(pick/total)