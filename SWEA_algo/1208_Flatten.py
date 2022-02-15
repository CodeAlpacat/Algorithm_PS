list_result = []
for _ in range(10):
    N = int(input())
    box_list = list(map(int, input().split()))
    list_count = [0] * 101
    for i in box_list:
        list_count[i] += 1 #각 박스 높이 값의 수를 셈.
    #0이 아닌 마지막 인덱스 -1 / 그 이전 인덱스 +1 / 맨 첫 번째 인덱스 -1 그 다음 인덱스 + 1
    max_num = max(box_list)
    min_num = min(box_list)
    # 박스가 하나 빠지면 층수가 하나 내려감.

    for _ in range(N):
        if min_num >= max_num:
            break
        list_count[max_num] -= 1
        list_count[max_num - 1] += 1

        list_count[min_num] -= 1
        list_count[min_num + 1] += 1

        if list_count[min_num] == 0:
            min_num += 1
        if list_count[max_num] == 0:
            max_num -= 1
        # 834에서 하나씩 줄어들어서 0되면 멈춤.
    list_result.append(max_num-min_num)

for i in range(len(list_result)):
    print(f'#{i+1} {list_result[i]}')