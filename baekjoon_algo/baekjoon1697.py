from collections import deque


N, K = map(int, input().split())
arr = [0 for _ in range(100001)]
def recur(cur):
    q = deque()
    q.append(cur)
    while q:
        n = q.popleft()
        
        if n == K:
            print(arr[n])
            return
        
        for i in (n - 1, n + 1, n * 2):
            if 0 <= i <= 100000 and not arr[i]:
                arr[i] = arr[n] + 1
                q.append(i) 


recur(N)