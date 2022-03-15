from collections import deque


T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))

    q = deque()
    for i in range(N):
        q.append([li[i], i])
    
    s = 0
    while len(q) != 1:
        q[0][0] //= 2
        
        if q[0][0] == 0:
            if N + s < M:
                q.popleft()
                q.append([li[N+s], N+s])
                s += 1
            elif N+s >= M:
                q.popleft()
            
        else:
            q.append(q.popleft())
    
    print(f'#{tc+1} {q[0][1]+1}')