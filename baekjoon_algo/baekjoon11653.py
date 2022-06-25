#소인수분해
N = int(input())

#1은 소수가 아니므로 따로 처리
X = N #N은 계속 나눠줘서 수가 변하기 때문에 X에 할당.
for i in range(2, N+1):
    if i * i > N:
        break
    
    while X % i == 0:
        print(i)
        X //= i
if X != 1:
    print(X)


##########

N = int(input())
ans = []
X = N

for i in range(2, N+1):
    if i * i > N:
        break
    
    while X % i == 0:
        ans.append(i)
        X //= i

for i in ans:
    print(i)
if X != 1:
    print(X)
else:
    pass