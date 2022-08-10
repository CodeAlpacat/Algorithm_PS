N = int(input())
mat = list(map(int, input().split()))
mat.sort()

M = int(input())
target_list = list(map(int, input().split()))

def binary(target):
    s = 0
    e = N-1
    flag = False
    while s <= e:
        m = (s + e) // 2
        if mat[m] == target:
            flag = True
            break
        elif mat[m] > target:
            e = m - 1
        else:
            s = m + 1
    if flag:
        return 1
    else:
        return 0

for i in target_list:
    print(binary(i))