N = int(input())
mat = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

cnt = {}

for i in range(N):
    cnt[mat[i]] = cnt.get(mat[i], 0) + 1

for i in range(M):
    print(cnt.get(cards[i], 0), end=' ')