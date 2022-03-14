N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
arr = []

def recur(cnt):
    
    arr.append(li[cnt])

    if len(arr) == M:
        print(*arr)
        return
    
    if cnt == N-1:
        return

    recur(cnt +1)
    recur(cnt)

recur(0)