#거스름돈 그리디 구현

n = 1260
count = 0

arr = [500, 100, 50, 10]

for coin in arr:
    count +=n //coin
    n %= coin

print(count)