N = int(input())

mat = [list(map(int, input().split())) for _ in range(N)]
mat.sort()
res = 0
for i in range(N):
    flag = False
    for j in range(N):
        if i != j:
            if mat[i][0] >= mat[j][0] and mat[i][1] >= mat[j][1]:
                flag = True
                continue
            elif mat[i][1] >= mat[j][1] and mat[i][0] >= mat[j][0]:
                flag = True
                continue
    
    if not flag:
        res += 1