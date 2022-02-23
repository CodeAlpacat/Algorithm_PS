#퀵정렬

def quickSort(a, begin, end):
    if begin < end :
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)

def partition (a, begin, end):
    pivot = (begin + end)//2
    L = begin
    R = end
    while L < R:
        while L < R and a[L] < a[pivot]:
            L += 1
        while L < R and a[R] >= a[pivot]:
            R += 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
    