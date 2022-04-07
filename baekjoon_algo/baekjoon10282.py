import sys
input = sys.stdin.readline

import heapq
inf = sys.maxsize
def get_dist(s):
    pq = []
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if d != dist[cur]:
            continue
        
        for i in range(len(mat[cur])):
            nxt = mat[cur][i][0]
            nd = dist[cur] + mat[cur][i][1]

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))


T = int(input())

for tc in range(T):
    n, d, c = map(int, input().split()) # 컴퓨터 개수, 의존성 개수, 해킹당한 컴 번호
    dist = [inf] * (n+1)
    mat = [[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split()) #a가 b를 의존하고 감염되면 s초 후 a 도 감염.
        mat[b].append([a, s])
        
    
    get_dist(c)
    max_num = 0
    cnt = 0
    for i in dist:
        if i != inf:
            max_num = max(max_num, i)
            cnt += 1
    print(cnt, max_num)