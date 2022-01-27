#블랙잭
#블랙잭 -> 카드의 합 <=21, 카드의 합을 최대로
#카드의 개수 N, 딜러가 정한 카드의 합 M
#풀이 = pick_card 리스트를 오름차순으로 정렬한 뒤, 브루트포스로 합을 전부 탐색.



N, M = map(int, input().split())

#5장의 카드를 공백 단위로 입력
pick_card = list(map(int, input().split()))

result =0
# 결과를 저장할 result 변수, 0~ N-1까지 탐색, j는 i다음 카드이므로 i+1부터 탐색, k는 j 다음 카드를 뽑아야함.
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            #서로 중복되지 않는 카드를 완전탐색
            if pick_card[i] + pick_card[j] + pick_card[k] > M:
                #M보다 크면 안됨.
                continue
            else:
                # result와 세 카드의 합 비교.
                result = max(result, pick_card[i] + pick_card[j] + pick_card[k])

print(result)