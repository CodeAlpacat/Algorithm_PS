from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

input = sys.stdin.readline
N, E = map(int, input().split())
v = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())
    v[a].append([b, c])
    v[b].append([a, c])


must_pass = list(map(int, input().split()))
must_pass.sort()

def get_dist(s , e):
    dist = [0xffffff] * (N+1)
    pq = []
    
    dist[s] = 0
    heapq.heappush(pq, [0, s])
    
    while pq:
        d, cur = heapq.heappop(pq)
        
        if cur == e:
            return d

        if d != dist[cur]:
            continue
        
        for i in v[cur]:
            nxt = i[0]
            nd = i[1] + dist[cur]

            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, [nd, nxt])
    return -1

a = get_dist(1, must_pass[0])
a1 = get_dist(1, must_pass[1])
b = get_dist(must_pass[0], must_pass[1])
c = get_dist(must_pass[1], N)
c1 = get_dist(must_pass[0], N)

if a + b + c < a1 + b + c1:
    if a == -1 or b == -1 or c == -1:
        if a1 == -1 or b == -1 or c1 == -1:
            print(-1)
        else:
            print(a1+b+c1)
    else:
        print(a+b+c)

elif a + b + c > a1 + b + c1:
    if a1 == -1 or b == -1 or c1 == -1:
        if a == -1 or b== -1 or c == -1:
            print(-1)
        else:
            print(a+b+c)
    else:
        print(a1+b+c1)

else:
    if a1 == -1 or b == -1 or c == -1 or a == -1 or b== -1 or c1 == -1:
        print(-1)
    else:
        print(a + b + c)
