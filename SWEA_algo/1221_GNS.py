arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
arr_2 = [0] * 10
# 0~ 9까지


T = int(input())

for x in range(T):
    tn, M = input().split()
    M = int(M)
    li = list(input().split())
    
    for i in range(len(li)):
        for j in range(len(arr)):
            if li[i] == arr[j]:
                arr_2[j] += 1
    print(f'#{x+1}', end =' ')
    for i in range(len(arr_2)):
        while arr_2[i] > 0:
            print(arr[i], end =' ')
            arr_2[i] -= 1
    print()