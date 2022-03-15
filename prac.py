
C = int(input())

def recur(cur, cnt):
    global ans
    

    if cur == 11:
        ans = max(ans, cnt)
        return

    for i in range(11):
        if visited_idx[i]:
            continue
        
        if li[cur][i]:
            visited_idx[i] = True
            recur(cur + 1, cnt + li[cur][i])
            visited_idx[i] = False



for _ in range(C):
    li = [list(map(int, input().split())) for _ in range(11)]
    visited_idx =[False] * 11
    ans = 0
    recur(0, 0)
    print(ans)
