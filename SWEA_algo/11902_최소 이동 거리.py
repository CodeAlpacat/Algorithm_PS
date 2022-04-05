import heapq


T = int(input())

for tc in range(1, T+1):
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for i in range(e):
        a, b, c = map(int, input().split())

        graph[a].append([b, c])

    dist = [0xffffff] * (n+1)

    pq = []
    dist[0] = 0
    heapq.heappush(pq, [0, 0])

    while len(pq):
        d, cur = heapq.heappop(pq)

        if dist[cur] != d:
            continue

        for i in range(len(graph[cur])):
            nxt = graph[cur][i][0]
            nd = dist[cur] + graph[cur][i][1]

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    
    print(dist[n])

