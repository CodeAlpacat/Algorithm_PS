# 버블 정렬
def bubbleSort(arr):
    # 배열의 크기만큼 반복
    for i in range(len(arr)):        
        # 배열의 총 크기에서 i와 1을 뺀 만큼 반복. 그 이유는 j의 현재 인덱스가 arr의 마지막 인덱스가 되면 j와 j+1을 비교할 때, indexOutofRange 이기 때문이다.
        for j in range(0, len(arr) - i - 1):
            # 만약 현재 인덱스의 값이 다음 인덱스보다 크면, 서로의 위치를 바꿈.
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]




arr_bubble = [4, 7, 80, 50, 30, 40, 20, 10]

bubbleSort(arr_bubble)
print(arr_bubble)