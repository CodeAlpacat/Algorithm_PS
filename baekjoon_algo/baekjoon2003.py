#수들의 합 2 => 투 포인터
#10 5
# 1 2 3 4 2 5 3 1 1 2
# s 시작
# e 시작
# s부터 e까지 합
#e가 순회하다가 합이 M이상이면 1로시작하는 것중 합이 M인 것은 없음.
#e가 안된다면 e는 고정된 상태에서 s만 증가함.
#M을 찾으면 s나 e나 무엇을 이동해도 상관없음.

N, M = map(int, input().split())
li = list(map(int, input().split())) + [0] #e가 끝까지 갔을 때, 런타임에러니 방지

s = 0
e = 0
total = li[0]
cnt = 0
#e가 끝까지 가면 끝남.
while e < N:
    if total == M:
        cnt += 1
        e += 1 #s던 e던 상관없음.
        total += li[e] #s를 증가시켜주면 arr[s]증가
    elif total < M:
        e += 1
        total += li[e]
    else:# total이 m보다 더 크다면 s 전진
        total -= li[s]
        s += 1

print(cnt)