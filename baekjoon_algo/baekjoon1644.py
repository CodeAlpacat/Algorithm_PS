###### 실패한 답
def recur(cur, total, flag):
    global ans

    if total and flag:
        if total == N:
            ans += 1
        return

    if total > N:
        return

    if total == N:
        ans += 1
        return

    if cur == len(prime_mat):
        return

    recur(cur + 1, total + prime_mat[cur], False)
    recur(cur + 1, total, True)

N = int(input())

prime_list = [True for _ in range(N+1)]
prime_list[0], prime_list[1] = False, False

for i in range(2, len(prime_list)):
    
    for j in range(i*i, N+1, i):
        if prime_list[j]:
            prime_list[j] = False

prime_mat = []
for i in range(len(prime_list)):
    if prime_list[i]:
        prime_mat.append(i)
ans = 0
recur(0, 0, False)

print(ans)

################ 정답


N = int(input())

prime_list = [True for _ in range(N+1)]
prime_list[0], prime_list[1] = False, False

for i in range(2, len(prime_list)):
    
    for j in range(i*i, N+1, i):
        if prime_list[j]:
            prime_list[j] = False

prime_mat = []
for i in range(len(prime_list)):
    if prime_list[i]:
        prime_mat.append(i)

prime_mat = prime_mat + [0]
s = 0
e = 0
total = prime_mat[0]
cnt = 0
while e < len(prime_mat)-1:
    
    if total < N:
        e += 1
        total += prime_mat[e]
    elif total > N:
        total -= prime_mat[s]
        s += 1
    else:
        cnt += 1
        e += 1
        total += prime_mat[e]

print(*prime_mat)
print(cnt)
