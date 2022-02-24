
li = []
total = 0
for i in range(9):
    N = int(input())
    li.append(N)
    total += N
ans = 0
li.sort()

def recur(cur, cnt, a):
    global ans
    if cnt > 2:
        return

    if cnt == 2:
        if total - a - li[cur] == 100:
            print(li[cur], a)
            return


    if cur == 8:
        return
    
    recur(cur + 1, cnt +1, a + li[cur])
    recur(cur + 1, cnt, a)


recur(0, 0, 0)