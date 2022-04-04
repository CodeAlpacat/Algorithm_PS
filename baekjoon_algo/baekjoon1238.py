import heapq

#정방향이면 해당 노드에서 다른 점들까지 최단거리를 구할 수 있다.
#역방향이면 다른 노드에서 현재 노드까지의 최단거리를 모두 구할 수 있다.
n, m, x = map(int, input().split())
v = [[] for _ in range(n+1)] #정방향 그래프
rv = [[] for _ in range(n+1)] #역방향 그래프

for i in range(m):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c]) #정방향
    rv[b].append([a, c]) #역방향

def get_dist(s, v): #s = 시작노드, v = v와 rv중 뭘쓸지
    pq = []
    
    dist[s] = 0
    heapq.heappush(pq, (0, s))
    while len(pq):
        d, cur = heapq.heappop(pq)

        if dist[cur] != d:
            continue

        for i in range(len(v[cur])):
            nxt = v[cur][i][0]
            nd = d + v[cur][i][1]

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))


dist = [1000000000 for _ in range(n+1)]
get_dist(x, v) #정방향 다익스트라
ans = dist[:]

dist = [1000000000 for _ in range(n+1)]
get_dist(x, rv) #역방향 다익스트라

for i in range(1, n+1):
    ans[i] += dist[i] #가는 길에서 오늘 길에 걸린 시간을 더함. ans = 정방향 복사 / dist = 다시선언해 역방향으로 구한 것.

mx = -1
for i in range(1, n+1):
    mx = max(mx, ans[i])

print(mx)