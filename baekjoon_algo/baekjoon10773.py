N = int(input())

ans = []
peak = 0
for i in range(N):
    K = int(input())
    if K == 0:
        ans.pop()
    else:
        ans.append(K)

print(sum(ans))