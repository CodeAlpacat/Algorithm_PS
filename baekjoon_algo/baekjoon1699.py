# N = int(input())

# def recur(cur, cnt):
#     global res

#     if cnt > N:
#         return

#     if cnt == N:
#         res = min(cur, res)
#         return

#     for i in range(1, N+1):
#         if i * i > N:
#             continue
#         recur(cur + 1, cnt + i*i)

# res = 10000000000
# recur(0, 0)
# print(res)



N = int(input())

def recur(cur):

    if cur < 0:
        return 1000000000

    if cur == 0:
        return 0

    if memo[cur] != 100000000:
        return memo[cur]

    for i in range(1, N+1):
        if i * i > N:
            continue
        memo[cur] = min(recur(cur - i*i) + 1, memo[cur])
    
    return memo[cur]

memo = [100000000] * 100010
print(recur(N))