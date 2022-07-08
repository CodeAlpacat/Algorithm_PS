N = int(input())
K = int(input())
#1, 2, 3, 4, 6, 8, 9
cnt = 0
for i in range(2, N+1):
    
    save = i
    mat = set([1])
    for j in range(2, i+1):
        if j * j > i:
            break

        while save % j == 0:
            mat.add(j)
            save //= j
    mat.add(save)
    
    if max(mat) <= K:
        cnt += 1

print(cnt+1)