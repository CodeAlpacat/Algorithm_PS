#N과 M (2)
#1부터 N까지 중복 없이 M개를 고른 수열

N, M = map(int, input().split())
li = [i for i in range(1, N+1)]
visited = [False for _ in range(N+1)]
li2 = []
def recur(cur):
    if len(li2) > M:
        return

    if len(li2) == M:
        print(*li2)
        return

    for i in range(cur, N+1):
        if visited[i]:
            continue
        
        li2.append(i)
        visited[i] = True
        recur(i+1)
        visited[i] = False
        li2.pop()

recur(1)