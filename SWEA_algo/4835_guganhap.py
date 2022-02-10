T = int(input())

result_list = []
for x in range(T):
    N, M = map(int, input().split())
    list_num = list(map(int, input().split()))
    #초기값
    max = 0
    min = 0
    for i in range(M):
        max += list_num[i]
        min += list_num[i]

    for i in range(M-1, len(list_num)):
        new_sum = 0
        for j in range(M):
            new_sum += list_num[i - j] # 5개의 구간합 5일때, 4 3 2 1 0/

        if new_sum > max:
            max = new_sum

        if new_sum < min:
            min = new_sum

    result_list.append(max - min)

for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')