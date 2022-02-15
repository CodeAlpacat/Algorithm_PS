n = int(input())
arr = list(map(int, input().split()))
arr2 = [0 for i in range(n)]
visited = [False for i in range(n)]
ans = 0
def recur(cur):
    global ans

    #기저조건
    if cur == n:
        total = 0
        for i in range(1, n):
            total += abs(arr2[i] - arr2[i-1])
        
        ans = max(ans, total)
        return
    
    # 재귀호출
    for i in range(n):
        if visited[i]:
            continue

        arr2[cur] = arr[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0) #0부터 중복제거한 전체 탐색

print(ans)