def recur(cur):
    global ans

    if cur == N:
        ans += 1
        return
    
    for i in range(N):
        if visited[i]:
            continue
        arr[cur] = i
        flag = True
        for j in range(cur): #중복이 없는 순열이므로 같은 y좌표
            if abs(arr[cur] - arr[j]) == abs(cur - j):
                flag = False
                break
        if flag:
            visited[i] = True # 0,0 0,1 0,2 0,3 다음 줄의 x축의 같은 y값은 고를 수 없다.
            recur(cur + 1)
            visited[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    visited = [False] * N
    ans = 0
    
    recur(0)
    print(f'#{tc} {ans}')