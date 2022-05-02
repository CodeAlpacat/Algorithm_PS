import sys
 
input = sys.stdin.readline
MOD=1000000007
n = int(input())
s = input()
w=0
h=0
e=0
ans=0
for c in s:
    if c=="W":
        w+=1
    elif c=="H":
        h+=w
    elif c=="E":
        ans=(2*ans+e)%MOD
        e+=h
print(ans)



#################

import sys
input = sys.stdin.readline
N = int(input())
input_mat = list(input())
mat = []
cnt = 0
W_list = []
H_list = []
for i in range(len(input_mat)):
    if input_mat[i] == 'W':
        mat.append(input_mat[i])
        cnt += 1
    elif input_mat[i] == 'H':
        mat.append(input_mat[i])
        cnt += 1
    elif input_mat[i] == 'E' and cnt > 1:
        mat.append(input_mat[i])

#W의 인덱스 저장 recur(W인덱스가 시작)
#각 H 인덱스 저장

for i in range(len(mat)):
    if mat[i] == 'W':
        W_list.append(i)
    elif mat[i] == 'H':
        H_list.append(i)


def recur(cur, cnt):

    if cur > end_point:
        return 0

    if cur == end_point:
        if cnt % 1000000007 > 1:
            return 1
        else:
            return 0

    if memo[cur][cnt] != -1:
        return memo[cur][cnt]

    memo[cur][cnt] = recur(cur + 1, (cnt + 1) % 1000000007) % 1000000007 + recur(cur + 1, cnt % 1000000007) % 1000000007 
    return memo[cur][cnt]

ans = 0
E_cnt = []
for i in W_list:
    for j in H_list:
        if i < j:
            count = 0
            for k in range(j, len(mat)):
                if mat[k] == 'E':
                    count += 1
            E_cnt.append(count)


for i in range(len(E_cnt)):
    memo = [[-1] * (E_cnt[i]) for _ in range(E_cnt[i])]
    end_point = E_cnt[i]
    ans += recur(0, 0)

print(ans)