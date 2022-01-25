T  = int(input())

for i in range(T):
    N = int(input())
    result_min = 0
    result_max = 0
    list_num = list(map(int, input().split()))
    for k in range(len(list_num)):
        if min(list_num) == list_num[k]:
            result_min = k
            break
        else:
            continue
        
    for k in range(len(list_num)):
        if max(list_num) == list_num[k]:
            result_max = k
            continue
        else:
            continue
    print(f'#{i+1}', abs(result_max - result_min), end =' ')
    print()

