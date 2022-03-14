#N과 M(11)
N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
visited = [False] * len(li)
arr = []
def recur(cur, cnt):
    
    if cur == M:
        print(*arr)
        return
        
    record = 0
    for i in range(N):
        if visited[i] or record == li[i]:
            continue
        
        arr.append(li[i])
        record = li[i]
        recur(cur + 1, i + 1)
        arr.pop()
        
recur(0, 0)