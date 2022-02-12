#덩치
# 사람 수 - 자기 자신보다 작지 않은 사람의 수

N = int(input())
list_person = []
result_list = []
for _ in range(N):
    A = list(map(int, input().split()))
    list_person.append(A)

for i in range(N):
    count = 0
    for j in range(N):
        #작을 때는 안셈.
        if list_person[i][0] < list_person[j][0] and list_person[i][1] < list_person[j][1]:
            pass
        #자기 자신까지 셋으니 1 빼줘야함.
        else:
            count += 1
    result_list.append(N-count+1)

for i in result_list:
    print(i, end=' ')
  