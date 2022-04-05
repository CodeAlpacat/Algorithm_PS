import heapq


N, M = map(int, input().split())
s = int(input())
v = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())

    v[a].append([b, c])

dist = [1000000000 for i in range(N+1)]
visited = [False for _ in range(N+1)]

pq = []
dist[s] = 0
heapq.heappush(pq, (0, s))
while len(pq) > 0:
# for _ in range(N): 이건 N번안돌수도, N번보다 더 돌아야할 수 있어서 불완전함.
    # mn = 1000000000
    # cur = 0
    # for i in range(1, N+1):
    #     if not visited[i] and dist[i] < mn:   
    #         mn = dist[i]
    #         cur = i
    d, cur = heapq.heappop(pq) #가장 작은 값 뽑힘. d = 현재 인덱스까지의 가중치합. cur = 인덱스 // O(logn)임 heappush, pop 둘다.
    
    if dist[cur] != d: #들어갔던 값에서 작은 값이 갱신되었다는 의미.
        continue
    
    # if visited[cur]: 위와 동치
    #     continue
    # visited[cur] = True

    for i in range(len(v[cur])): # 간선의 개수만큼 반복. 각 노드마다 이어진 간선만큼 반복함.
        nxt = v[cur][i][0] # 노드번호
        nd = dist[cur] + v[cur][i][1] #현재가중치 + 가중치 = 다음까지의 거리
        
        if dist[nxt] > nd: #다음인덱스는 INF거나 이미 값이 있음. 가중치가 더 작다면 바꿔줌.
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, N+1):
    if dist[i] == 1000000000:
        print('INF')
    else:
        print(dist[i])