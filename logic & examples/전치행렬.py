arr = [
    [1, 0, 0, 0, 0],
    [3, 4, 5, 6, 7],
    [1, 3, 5 ,6, 8],
    [7, 8, 9, 6, 4]
]

N = 5
for r in range(N):
    for c in range(N):
        if r<c:
            print(arr[r][c])



#----------------------- 두 식은 같음.
for r in range(N-1):
    for c in range(r+1, N):
        print(arr[r][c])


#------------------- 두 개 뽑기
for i in range(N-1):
    for j in range(i+1, N):
        print(arr[i], arr[j])

#----------------- 세 개
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N-2):
            print(arr[i], arr[j], arr[k])
