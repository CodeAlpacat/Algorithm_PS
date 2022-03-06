#N과 M (4)
N, M = map(int, input().split())
li2 = []
def recur(cur):
    if len(li2) > M:
        return

    if len(li2) == M:
        print(*li2)
        return

    for i in range(cur, N+1):
        li2.append(i)
        recur(i)
        li2.pop()

recur(1)