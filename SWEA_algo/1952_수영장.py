T = int(input())

def recur(cur, cnt):
    global ans   

    if cur > len(plan):
        return

    if cur == len(plan):
        ans = min(ans, cnt)
        return

    recur(cur + 1, cnt + price[0]*plan[cur])
    recur(cur + 1, cnt + price[1])
    recur(cur + 3, cnt + price[2])


for tc in range(T):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = 1000000000
    recur(0, 0)
    if ans > price[3]:
        ans = price[3]
        print(f'#{tc+1} {ans}')
    else:
        print(f'#{tc+1} {ans}')


#메모이제이션

T = int(input())

def recur(cur):  

    if cur > len(plan):
        return 0

    if cur == len(plan):
        return 0

    if memo[cur] != -1:
        return memo[cur]
    memo[cur] = min(recur(cur + 1) + price[0]*plan[cur], recur(cur + 1) + price[1], recur(cur + 3) + price[2])
    return memo[cur]

for tc in range(T):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    memo = [-1] * (len(plan) +1)
    a = recur(0)
    if a > price[3]:
        a = price[3]
        print(f'#{tc+1} {a}')
    else:
        print(f'#{tc+1} {a}')