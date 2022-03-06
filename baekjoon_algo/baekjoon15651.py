#N과 M (3)

N, M = map(int, input().split())
li = []
def recur(cur):
    
    if len(li) > M:
        return

    if len(li) == M:
        print(*li)
        return

    for i in range(1, N+1):
        li.append(i)
        recur(cur+1)
        li.pop()
        
recur(0)