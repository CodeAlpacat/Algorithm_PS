#돌게임3
N = int(input())
ans = ''
dp = [False] * 1010
def recur(cur, cnt):
    global ans
    
    
    if cur == N:
        if cnt % 2 == 1:
            ans = 'SK'
            return
        else:
            ans = 'CY'
            return
    if cur + 1 > N or cur + 3 > N or cur + 4 > N:
        return
    recur(cur + 1, cnt + 1)
    recur(cur + 3, cnt + 1)
    recur(cur + 4, cnt + 1)

recur(0, 0)
print(ans)
# cnt가 홀수이면 상근이 이김