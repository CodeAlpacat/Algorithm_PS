input = sys.stdin.readline

def recur(cur, total):
    global ans

    
    if cur == N:
        if total == S:
            ans += 1
        return

    recur(cur + 1, total + mat[cur])
    recur(cur + 1, total)

N, S = map(int, input().split())
mat = list(map(int, input().split()))
ans = 0
recur(0, 0)
if S == 0:
    print(ans-1)
else:
    print(ans)