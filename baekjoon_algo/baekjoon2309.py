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

##################################

mat = []
total_spy = -100
for i in range(9):
    N = int(input())
    mat.append(N)
    total_spy += N

mat.sort()
s = 0
e = 8

while s < e:
    
    if mat[s] + mat[e] < total_spy:
        s += 1
    elif mat[s] + mat[e] > total_spy:
        e -= 1
    else:
        break

for i in range(len(mat)):
    if i == s or i == e:
        continue
    print(mat[i])
