#1이 될 때까지 아래를 수행한다.
#N과 K가 공백 단위로 입력되고, N이 1이 될 때까지
#1. N에서 -1
#2. N에서 K를 나눔.
#이 과정의 최소값을 구해야함.

N, K = map(int, input().split())
count = 0 # 횟수를 저장
while True:
    if N % K == 0:
        N //= K
        count +=1
    else:
        N -= 1
        count +=1
    
    if N < K:
        break

print(count)

