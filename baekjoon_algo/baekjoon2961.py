#도영가 만든 맛있는 음식
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 1<< 60

def recur(cur, cnt, a, b):
    global ans

    if cnt != 0: #O의 개수가 0개만 아니면 된다. 신맛쓴맛을 사용한다.
        ans = min(ans, abs(a - b)) # ans와 신맛쓴맛의 차 비교
    
    if cur == n: #끝까지 들어감
        return
    
    recur(cur+1, cnt+1, a * arr[cur][0], b + arr[cur][1]) #현재 신맛 쓴맛에 곱
    recur(cur+1, cnt, a, b) #고르지 않음.
    #이 두 재귀로 고르고 고르지 않고의 모든 경우의 수를 탐색 가능.

recur(0, 0, 1, 0)
print(ans)