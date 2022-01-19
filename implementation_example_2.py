#시각
#24이하의 정수 N 입력
#모든 시각에서 3이 하나라도 포함되는 모든 경우의 수를 구함.
# 00시 00분 00초 ~ N시 59분 59초까지

#풀이 ->N이 1을 입력받으면
#00.00.03, 00.00.13. 00.00.23.. 00.00.30~39 ... 00.00.53 -> 매 분 확정 15개
#00.03.xx 일 때, 00~59까지 -> 60개
#... 모든 경우의 수를 나눌 수 없으니 완전 탐색으로 풀어야한다.

N = int(input())

count_hour, count_min, count_sec = 0, 0, 0
count_result = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count_result += 1

print(count_result)