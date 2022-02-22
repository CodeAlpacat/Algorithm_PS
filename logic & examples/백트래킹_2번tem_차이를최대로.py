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
        visited[i] = True # 이전 값들의 중복을 True로 바꿔 제거한다. 앞의 continue 문0
        recur(cur + 1)
        visited[i] = False # 다시 초기화

recur(0) #0부터 중복제거한 전체 탐색

print(ans)