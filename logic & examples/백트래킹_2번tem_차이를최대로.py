n = int(input())
arr = list(map(int, input().split()))
arr2 = [0 for i in range(n)]
visited = [False for i in range(n)]

def recur(cur):
    if cur == n:
        total = 0
        for i in range(1, n):
            total += abs(arr[arr2[i]]) - arr[i-1]
        return
    
    for i in range(n):
        if visited[i]:
            continue

        arr2[cur] = i