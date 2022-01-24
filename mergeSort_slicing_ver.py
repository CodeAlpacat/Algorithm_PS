#합병정렬 기본 예시 / 슬라이싱을 이용하므로 공간복잡도 최악. 100만개짜리 리스트면 50만개 + 50만개 식으로 계속 리스트 생성.
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    #분할 정복의 과정
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    #합병의 과정
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr