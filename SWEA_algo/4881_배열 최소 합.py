#4881 배열 최소 합

T = int(input())

def recur(cur, sum_row):
    global total
    
    if sum_row > total:
        return

    if cur == N:
        if sum_row < total:
            total = sum_row
            return
    
    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = True
        recur(cur+1, sum_row + li[cur][i]) #x축은 깊이인 li[0] li[1] li[2]기준으로 3가지 경우 복사
        visited[i] = False # x축 1증가하고 그 중에 고르는 경우.

for t in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    total = 0 #전체의 합
    for i in li:
        total += sum(i)

    recur(0, 0)
    print(f'#{t+1} {total}')