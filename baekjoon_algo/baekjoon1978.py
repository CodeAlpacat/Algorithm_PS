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