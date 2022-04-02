from collections import deque

T = int(input())

def recur(cur):
    q = deque()
    q.append(cur)
    while q:
        n = q.popleft()

        if n == M:
            return arr[n]

        for i in (n - 1, n + 1, n * 2, n - 10):
            if 0 <= i <= 1000000 and not arr[i]:
                arr[i] = arr[n] + 1
                q.append(i)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0 for _ in range(1000001)]

    print(f'#{tc} {recur(N)}')