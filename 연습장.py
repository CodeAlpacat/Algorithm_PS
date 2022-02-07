#소인수분해
N = int(input())

#1은 소수가 아니므로 따로 처리
X = N #N은 계속 나눠줘서 수가 변하기 때문에 X에 할당.
for i in range(2, N+1):
    #소인수가 루트N보다 큰게 많아봐야 1개임. 두 수 이상이면 N보다 커짐.
    if i * i > N:
        break
    
    while X % i == 0:
        print(i)
        X //= i
#마지막은 1이 될때까지 나눴거나, 나뉘지 않는 소수이므로, 1이 아니라면 X를 출력한다.
if X != 1:
    print(X)