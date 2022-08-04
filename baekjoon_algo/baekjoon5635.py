N = int(input())

mat = [list(input().split()) for _ in range(N)]

mat = sorted(sorted(sorted(mat, key=lambda x: int(x[-3])), key=lambda y: int(y[-2])), key=lambda z: int(z[-1]))

print(mat[-1][0])
print(mat[0][0])