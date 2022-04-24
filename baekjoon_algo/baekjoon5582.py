import sys
input = sys.stdin.readline
A = list(input())
B = list(input())
max_len = -0xffffff
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            idx = [i, j]
            cnt = 0
            while idx[1] < len(B) and idx[0] < len(A) and A[idx[0]] == B[idx[1]]:
                cnt += 1
                idx[0] += 1
                idx[1] += 1
            max_len =max(max_len, cnt)
if max_len < 0:
    print(0)
else:
    print(max_len)