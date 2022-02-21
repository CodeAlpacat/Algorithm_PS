arr_bubble = [9 ,5, 4, 80, 50, 30, 40, 20, 10]

#부분집합순열
for i in range(1<<len(arr_bubble)):
    for j in range(len(arr_bubble)):
        if i & (1<<j):
            print(j, end = ' ')
    print()


#카운팅정렬
def counting(a, k):
    c = [0] * (k+1)
    res = [0] * len(a)

    for i in range(len(a)):
        c[a[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    for i in range(len(a)-1, -1, -1):
        c[a[i]] -= 1
        res[c[a[i]]] = a[i]
    return res
#버블정렬

def bubble(arr):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
#선택정렬

def selection(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

#이진탐색
def binary(arr, target):
    s = 0
    e = len(arr)-1
    
    while s <= e:
        m = (s+e) // 2

        if arr[m] > target:
            e = m - 1
        elif arr[m] < target:
            s = m + 1
        else:
            return m
    return -1

#전치행렬
arr = [ [ 1,  0,  0,  0,  0],
        [ 6,  7,  0,  0,  0],
        [11, 12, 13,  0,  0],
        [16, 17, 18, 19,  0],
        [21, 22, 23, 24, 25]]
N = 5

for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#델타

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, 1, -1]

N = 9
arr = [[' '] * N for _ in range(N)]
r, c = 4, 4

for i in range(4):
    nr, nc = r, c
    while 0 <= nr + dr[i] < N and 0 <= nc + dc[i] < N:
        nr, nc = nr + dr[i], nc + dc[i]
        arr[nr][nc] = i + 1

for lst in arr:
    print(*lst)