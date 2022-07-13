N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())

set_M = []
cnt = 0
for i in range(M):
    if input() in S:
        cnt += 1
print(cnt)