def recur(cur, cnt):

    if cur == n:
        if cnt == m:
            return 1
        else:
            return 0
        
    if memo[cur][cnt] != -1:
        return memo[cur][cnt]

    memo[cur][cnt] = recur(cur + 1, cnt + 1) + recur(cur + 1, cnt)
    return memo[cur][cnt]

n, m = map(int, input().split())
memo = [[-1] * (n+1) for _ in range(n+1)]

print(recur(0, 0))