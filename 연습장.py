N = int(input())
# 제곱수 찾기
count = 1 #1도 제곱수
for i in range(2, N+1):
    if i*i > N:
        break
    count += 1
    
print(count)