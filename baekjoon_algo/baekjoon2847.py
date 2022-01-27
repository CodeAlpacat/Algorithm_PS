#게임을 만든 동준이
# N개의 레벨이 있다. 레벨 클리어 = 점수 보상
# 실수로 쉬운 레벨이 어려운 레벨보다 점수를 많이 받음.
#1씩 몇 번 감소시켜야 클리어인지
N = int(input())

score_list = []
for _ in range(N):
    score_list.append(int(input()))
count = 0 #몇 번 바꿨는가
for i in range(len(score_list)-1, 0, -1): #두 번째 인자부터 끝까지 비교.
    while True:
        if score_list[i] <= score_list[i-1]:
            score_list[i-1] -= 1
            count += 1
        else:
            break

print(count)