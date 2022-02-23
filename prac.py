#블랙잭 백트래킹 조합(중복x)

N, M = map(int, input().split())
li = []
visited = [False] * (N+1)
def recur(cur):
    
    if cur == M:
        print(*li)
        return


    for i in range(1, N+1):
        if visited[i]:
            continue
        
        li.append(i)
        visited[i] = True
        recur(cur+1)
        visited[i] = False
        li.pop()

recur(0)