
T = int(input())
def recur(total):
    global res

    if total > N:
        return

    if total == N:
        res += 1
        return

    for i in range(1, 4):
        recur(total + i)
for i in range(T):
    N = int(input())
    res = 0
    recur(0)
    print(res)