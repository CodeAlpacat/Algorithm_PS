import sys
input = sys.stdin.readline

def recur(cur, s):

    if cur > 6:
        return
    if cur == 6:
        print(*li2)
        return
    
    for i in range(s, li[0]):
        if visited[i]:
            continue
        
        li2[cur] = li_real[i]
        visited[i] = True
        recur(cur+1, i + 1)
        visited[i] = False
while True:
    li = list(map(int, input().split()))
    if li[0] == 0:
        break
    li_real = li[1:]
    visited = [False] * li[0]
    li2 = [0] * 6
    
    recur(0, 0)
    print(' ')