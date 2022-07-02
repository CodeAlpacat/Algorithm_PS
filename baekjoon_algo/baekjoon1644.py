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

