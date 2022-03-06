#N과 M (6)
N, M = map(int, input().split()) #N개의 리스트에서 M개 고른 수열
li = list(map(int, input().split()))
li.sort()
li2 = []

def recur(cur):

    if len(li2) == M:
        print(*li2)
        return

    for i in range(cur, N):
        if li[i] in li2:
            continue

        li2.append(li[i])
        recur(i+1)
        li2.pop()
recur(0)