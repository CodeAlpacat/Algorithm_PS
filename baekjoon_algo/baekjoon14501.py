N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
ans = 0
def recur(cur, cnt):
    global ans

    if cur > N:
        return

    if cur == N:
        ans = max(ans, cnt)
        return

    recur(cur + li[cur][0], cnt + li[cur][1])
    recur(cur + 1, cnt)

recur(0, 0)
print(ans)


N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
memo = [-1] * 15010 # 입력


def recur(cur):

    if cur > N:
        return -1000000

    if cur == N:
        return 0

    if memo[cur] != -1:
        return memo[cur]

    memo[cur] = max(recur(cur + li[cur][0]) + li[cur][1], recur(cur + 1))
    return memo[cur]

print(recur(0))
