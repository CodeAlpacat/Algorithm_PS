#소수 찾기
N = int(input())
num_list = list(map(int, input().split()))

result=0
for i in num_list:
    cnt = 0
    for j in range(1, i+1): #1과 자기자신만 나와야 소수이므로 cnt가 2이면 소수이므로 result + 1
        if i%j == 0:
            cnt +=1
    if cnt == 2:
        result += 1
    else:
        pass

print(result)


################


def isPrime(a):
    
    cnt = 0
    if a == 1:
        return 0

    for i in range(2, a+1):
        if i * i > a:
            break

        if a % i == 0:
           cnt += 1
    
    if cnt == 0:
        return 1
    else:
        return 0

N = int(input())
mat = list(map(int, input().split()))
ans = 0
for i in mat:
    ans += isPrime(i)

print(ans)