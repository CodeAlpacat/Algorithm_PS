# def merge_sort(arr):
#     def sort(low, high):
#         if high - low < 2:
#             return
#         mid = (low + high) // 2
#         sort(low, mid)
#         sort(mid, high)
#         merge(low, mid, high)

#     def merge(low, mid, high):
#         temp = []
#         l, h = low, mid

#         while l < mid and h < high:
#             if arr[l] < arr[h]:
#                 temp.append(arr[l])
#                 l += 1
#             else:
#                 temp.append(arr[h])
#                 h += 1

#         while l < mid:
#             temp.append(arr[l])
#             l += 1
#         while h < high:
#             temp.append(arr[h])
#             h += 1

#         for i in range(low, high):
#             arr[i] = temp[i - low]

#     return sort(0, len(arr))

#######################################
#기본 탬플릿
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    #분할 / 정복
    mid = len(lst) // 2
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])

    ret = []
    while l and r:
        if l[0] < r[0]:
            ret.append(l.pop(0))
        else:
            ret.append(r.pop(0)) #큐로 구현해야함.
    ret.extend(l)
    ret.extend(r)
    return ret


arr = [69, 10, 30, 2, 16, 8, 31, 22]


merge_sort(arr)


############################################
#C 언어 스타일

def merge_sort(s, e):
    if s == e:
        return
    
    mid = (s+e) // 2
    merge_sort(s, mid)
    merge_sort(mid+1, e)

    i, j, k = s, mid+1, s
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k, i = k+1, i+1
        else:
            tmp[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]
        k, i = k+1, i+1
    while j <= e:
        tmp[k] = arr[j]
        k, j = k + 1, j + 1
    
    for i in range(s, e+1):
        arr[i] = tmp[i]



arr = [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)
tmp = [0] * N #병합된 결과 저장
merge_sort(arr)