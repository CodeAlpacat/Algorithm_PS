# import sys
# sys.stdin=open('sample_input.txt')

def recur(cur):
    global ans

    if cur == N:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == arr[j]:
                    return
        else:
            ans += 1
        return

    for i in range(N):
        
        if cur == i:
            continue

        arr[cur] = i # [cur, i] = [x, y]
        recur(cur + 1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    visited = [False] * N
    ans = 0
    
    recur(0)
    print(ans)