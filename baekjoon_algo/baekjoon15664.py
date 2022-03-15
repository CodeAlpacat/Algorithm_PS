#N과 M(10)
N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
arr = []

def recur(cur, cnt):
    
    if cur == M:
        print(*arr)
        return

    record = 0
    for i in range(cnt, N):
        if record == li[i]:
            continue
  
        arr.append(li[i])
        record = li[i]
        recur(cur + 1, i + 1)
        arr.pop()

recur(0, 0)