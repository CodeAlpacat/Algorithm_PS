li = []
for i in range(9):
    N = int(input())
    li.append(N)
ans = []

visited = [False] * 9
li2 =[0] * 7

def recur(cur, total):
    global ans
    if total > 100:
        return
        
    if cur == 7:
        if total == 100:
            ans = sorted(li2)
        return

    for i in range(9):
        if visited[i]:
            continue

        li2[cur] = li[i]
        visited[i] = True
        recur(cur + 1, total + li[i])
        visited[i] = False

recur(0, 0)

for i in ans:
    print(i)