import heapq
T = int(input())

def get_dist(s, mat):
    pq = []
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if dist[cur] != d:
            continue

        for i in range(len(mat[cur])):
            nxt = mat[cur][i][0]
            nd = dist[cur] + mat[cur][i][1]
            
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    
    
    v = [[] for _ in range(N+1)]
    rv = [[] for _ in range(N+1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        
        v[x].append([y, c]) #정방향
        rv[y].append([x, c]) #역방향

    dist = [0xffffff] * (N+1)
    get_dist(X, v)
    ans = dist[:]

    dist = [0xffffff] * (N+1)
    get_dist(X, rv)

    for i in range(1, N+1):
        ans[i] += dist[i] #오고 가는 시간 더하기
    
    max_res = -1000000000
    for i in range(1, N+1):
        if max_res < ans[i]:
            max_res = ans[i]

    print(f'#{tc} {max_res}')