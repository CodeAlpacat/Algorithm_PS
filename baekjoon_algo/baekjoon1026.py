N = int(input())
mat = sorted(list(map(int, input().split())))
mat2  = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(N):
    ans += mat[i] * mat2[i]

print(ans)