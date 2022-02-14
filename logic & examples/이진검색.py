#이진 검색
#정렬된 자료로 중앙값과 비교해 크면 오른쪽, 작으면 왼쪽 탐색
def binarySearch(a, N, key): #a = 정렬된 배열, N = 길이, Key = 구할 수
    start  = 0 
    end = N-1
    while start <= end:
        middle = (start + end) //2
        if a[middle] == key: #검색 성공
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False #검색 실패

#------------------------ 재귀

def binarySearch2(a, low, high, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            return binarySearch2(a, low, middle-1, key)
        else:
            return binarySearch2(a, middle+1, high, key)