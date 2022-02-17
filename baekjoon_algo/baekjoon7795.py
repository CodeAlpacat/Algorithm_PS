#먹을 것인가 먹힐 것인가
#A와 B 물고기 중에 A가 B보다 큰 쌍의 개수
def binarySearch(arr, target):
    start  = 0 
    end = len(arr)-1
    res = -1
    while start <= end:
        middle = (start + end) //2
        if arr[middle] >= target:
            end = middle - 1
        else:
            res = middle
            start = middle + 1
    return res #검색 실패
        


T = int(input())
list_li = []
for x in range(T):
    N, M = map(int, input().split()) # A물고기 B물고기 수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_s = sorted(A)
    B_s = sorted(B)
    
    cnt = 0

    for i in A_s:
        cnt += binarySearch(B_s, i) + 1
  
    list_li.append(cnt)

for i in list_li:
    print(i)

#이분 탐색
# 1 1 3 7 8
# s e
# 
# 1 3 6
#cnt = 1
#먹을 것인가 먹힐 것인가
#A와 B 물고기 중에 A가 B보다 큰 쌍의 개수