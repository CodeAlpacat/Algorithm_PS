N = int(input())

ans = 0
prev = -0xffffff
for tc in range(1, N+1):
    max_num = -0xffffff
    mat = list(map(int, input().split()))
    
    for i in range(len(mat)-2):
        for j in range(i+1, len(mat)-1):
            for k in range(j+1, len(mat)):
                if (mat[i] + mat[j] + mat[k]) % 10 > max_num:
                    max_num = (mat[i] + mat[j] + mat[k]) % 10
    if max_num >= prev:
        ans = tc
        prev = max_num

print(ans)