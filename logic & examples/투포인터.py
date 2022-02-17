#투포인터

#1. 특정 조건을 만족하는 연속 부분 수열을 찾는다.
#2. 특정 조건을 만족하는 두 개의 수를 찾는다.

#연속 부분 수열 => 투 포인터, prefix sum + binary search
# 1 5
# 1 5 8
# 5 8 7
#...

#부분 수열
# 1 5 8 7 3
# 1 8
# 1 8 7
# 1 7 8 -> 순서가 바뀌면 X

n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0] #e가 끝까지 갔을 때, 런타임에러니 방지

s = 0
e = 0
total = arr[0]
cnt = 0
#e가 끝까지 가면 끝남.
while e < n:
    if total == m:
        cnt += 1
        e += 1 #s던 e던 상관없음.
    elif total < m:
        e += 1 #맨 끝 인덱스에러 조심
    else:# total이 m보다 더 크다면 s 전진
        s += 1
        
print(cnt)