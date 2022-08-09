N, K = map(int, input().split())
mat = []
for i in range(N):
    mat.append(int(input()))
cnt = 0
for i in range(N-1, -1, -1):
    while mat[i] <= K:
        n, K = divmod(K, mat[i])
        cnt += n

print(cnt)