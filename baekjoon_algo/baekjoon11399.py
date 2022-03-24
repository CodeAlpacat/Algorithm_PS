def recur(cur, total, sum_time):
    global ans
    if cur == N:
        ans = min(ans, sum_time)
        return

    for i in range(len(P)):
        if visited[i]:
            continue

        li[cur] = P[i]
        li_ans[cur] = total + li[cur]
        visited[i] = True
        recur(cur + 1, total + li[cur], sum_time + li_ans[cur])
        visited[i] = False
    


N = int(input())
P = list(map(int, input().split()))
visited = [False] * len(P)
li = [0] * len(P)
li_ans = [0] * (len(P))
ans = 100000000
recur(0, 0, 0)
print(ans)



N = int(input())
P = list(map(int, input().split()))
P.sort()

ans = 0
for i in range(len(P)):
    for j in range(i+1):
        ans += P[j]

print(ans)