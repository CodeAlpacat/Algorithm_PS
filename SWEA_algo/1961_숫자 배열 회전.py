T = int(input())

for x in range(T):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    li_2 = list(map(list, zip(*li)))





# 1 2 3
# 4 5 6
# 7 8 9

# 1 4 7
# 2 5 8
# 3 6 9

#90도 = arr1[i][j] = arr[N-1-j][i]
#180도 = arr2[i][j] = arr[N-1-j][N-1-j]
#270도 = arr3[i][j] = arr[j][N-1-i]s
#for a1, a2, a3 in zip(aar1, arr2, arr3)
#print(''.join(map(str, a1) a2 a3))