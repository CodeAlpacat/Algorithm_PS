A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
arr = []
def recur(cur, cnt):

    if cur == len(A):
        if cnt == 0:
            print(*arr)
        return

    arr.append(A[cur])
    recur(cur + 1, cnt + A[cur])
    arr.pop()
    recur(cur + 1, cnt)


recur(0, 0)