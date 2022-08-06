N = int(input())
mat = []
for i in range(N):
    mat.append(input())


mat2 = sorted(mat)
mat3 = sorted(mat, reverse=True)
ans = ''
for i in range(N):
    if mat[i] != mat2[i]:
        break
else:
    ans = 'INCREASING'

for i in range(N):
    if mat[i] != mat3[i]:
        break
else:
    ans = 'DECREASING'

if not ans:
    ans = "NEITHER"
    
print(ans)