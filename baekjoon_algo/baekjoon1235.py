N = int(input())
mat = []
a = 0
for i in range(N):
    mat.append(input())

a = len(mat[0])
ans = 0
for i in range(a):
    student_set = set()
    for j in range(N):
        student_set.add(mat[j][a-i-1:a])
    
    if len(student_set) == N:
        ans = i + 1
        break
print(ans)