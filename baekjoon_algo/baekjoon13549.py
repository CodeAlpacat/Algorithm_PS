import heapq
import sys
input = sys.stdin.readline

def get_dist(n, k):
    if n >= k:
        print(n-k)
        return

    pq = []
    dist[n] = 0
    heapq.heappush(pq, (0, n))
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if d != dist[cur]:
            continue
        
        for i in [cur-1, cur+1, cur * 2]:
            if 0 <= i <= 100000:
                nxt = i
                if i == cur * 2 and dist[i] == 0xffffff:
                    nd = d
                elif dist[i] == 0xffffff:
                    nd = d + 1
                
                if dist[nxt] == 0xffffff:
                    dist[nxt] = nd
                    heapq.heappush(pq, (nd, nxt))
    print(dist[k])

N, K = map(int, input().split())
dist = [0xffffff] * (100010)

get_dist(N, K)