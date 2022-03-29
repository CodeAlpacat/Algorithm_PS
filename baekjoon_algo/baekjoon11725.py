import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

par  = [0] * (N+1)
def dfs(cur, prv):
    par[cur] = prv #현재의 부모노드는 prv이다.

    for nxt in arr[cur]:
        if nxt == prv:
            continue
        dfs(nxt, cur) #현재 노드를 다음 재귀의 부모로 넘겨줌.

dfs(1, -1)

for i in range(2, N+1):
    print(par[i])