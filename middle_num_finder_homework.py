def counting_sort(list_num, N): #N은 list_num에 들어갈 수 중 가장 큰 수
    new_list = [0 for _ in range(N)] # 값의 count값이 들어갈 리스트
    sorted_list =[0 for _ in range(len(list_num))] # 정렬된 결과가 들어갈 리스트
    
    for i in list_num:
        new_list[i] += 1 #list_num의 값에 해당하는 인덱스 + 1 씩
    
    for i in range(1, N):
        new_list[i] += new_list[i-1] #값들의 누적합
    
    for i in range(len(list_num)):
        sorted_list[new_list[list_num[i]]-1] = list_num[i] # sorted_list에 차례로 할당.
        new_list[list_num[i]] -= 1 

    return sorted_list



numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

result_sorted= counting_sort(numbers, 100)
if len(numbers) % 2 == 0:
    print((result_sorted[len(result_sorted)//2 - 1] + result_sorted[len(result_sorted)//2])/2)
else:
    print(result_sorted[len(result_sorted)//2])
