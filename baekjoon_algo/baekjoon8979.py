#올림픽
#올림픽의 비공식 순위를 정하는 문제
#1. 금메달이 많음 2. 금이 같으면 은이 많은나라가 순위가 높음. 3. 금은이 다 많으면 동이 많은 나라.
#나라는 각각 1~N 사이의 정수로 표현.
#4개의 국가 중   1등 공동2등이 있다면, 3등은 없이 4등이다.
N, K = map(int, input().split())
list_country = [[] for _ in range(N)] # 2중 리스트 나라 순서대로 금은동이 기록됨.
for _ in range(N):
    country_num, gold, silver, bronze = map(int, input().split())
    list_country[country_num-1] = [gold, silver, bronze] #국가 1은 0번인덱스에 저장 ... 
gold_K, silver_K, bronze_K = list_country[K-1] # K번 국가의 금 은 동

count = 1

for i in range(N):
    if gold_K < list_country[i][0]: # [i][0]은 금메달
        count += 1
    elif gold_K == list_country[i][0]: #같을때
        if silver_K < list_country[i][1]: #은메달 비교
            count += 1
        elif silver_K == list_country[i][1]: #은메달이 같을 때,
            if bronze_K < list_country[i][2]:
                count += 1

print(count)