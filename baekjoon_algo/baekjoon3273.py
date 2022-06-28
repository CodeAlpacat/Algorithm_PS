n = int(input())
mat = list(map(int, input().split()))
x = int(input())
mat.sort()
s = 0
e = len(mat) - 1
cnt = 0
while s < e:
    
    if mat[s] + mat[e] < x:
        s += 1
    
    elif mat[s] + mat[e] > x:
        e -= 1
    
    else:
        cnt += 1
        s += 1

print(cnt)