#소인수 분해하고 그 결과에 A가 포함되면 A의 개수만큼만 출력

N, A = map(int, input().split())
cnt = 0

for i in range(N, A-1, -1):
    
    num = i
    while num % A == 0:
        cnt += 1
        num //= A
    

print(cnt)

##########################################


n, a = map(int, input().split())
m = n // a  # a의 배수의 개수
cnt = m     # cnt는 a의 배수의 개수를 담는다.

# cnt에 A의 배수의 개수를 담고
# 반복문 한 번 시행 : A^2의 배수의 개수를 담고
# 반복문 두 번 시행 : A^3의 배수의 개수를 담는다.
# 반복문 N 번 시행 : A^N의 배수의 개수를 담는다.
# 위 반복문을 반복해 A의 총 누적곱을 담는 것이다.
while m >= a:
    m //= a     # 반복문을 시행할수록 a^(시행횟수+1)의 배수의 개수
    cnt += m

print(cnt)