#거스름돈 그리디 구현

n = 1260
count = 0

arr = [500, 100, 50, 10]

for coin in arr:
    count +=n //coin
    n %= coin # 가장 큰 coin부터 모두 사용하므로 coin보다 무조건 작아야만 한다.

print(count)