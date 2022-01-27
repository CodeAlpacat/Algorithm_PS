#선택 정렬
def select_sort(list_num):

    for i in range(0, len(list_num) - 1): # 마지막 index는 비교할 대상이 없음.
        min_idx = i # 탐색 과정에서 가장 작은 값을 찾아 현재 인덱스와 바꿔줄 변수를 초기화.
        for j in range(i + 1, len(list_num)): #두 번째 인덱스부터 끝까지 탐색.
            if list_num[j] < list_num[min_idx]: # 현재 인덱스의 값과 다음 인덱스들인 list_num[j]의 값을 비교해 최소값을 찾아 min_idx에 저장한다.
                min_idx = j

        list_num[i], list_num[min_idx] = list_num[min_idx], list_num[i] # 순회 후에 가장 작은 인덱스의 값과 현재 인덱스를 바꿔준다.
    return list_num
 
print(select_sort([2, 4, 5, 1, 3, 4, 7, 30]))