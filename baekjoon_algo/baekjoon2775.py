#부녀회장이 될테야
N = int(input())
result_list = []
for i in range(N):
    K, n = int(input()), int(input())
    # 0~k층까지이므로 k층포함
    # 호수는 1부터 시작 N까지 반복
    arr = [[0 for _ in range(15)] for _ in range(15)]
    for j in range(K+1):
        for k in range(1,n+1):
            if j == 0:
                arr[j][k] = k
            else: #j-1층의 k호까지의 합
                for g in range(1, k+1):
                    arr[j][k] += arr[j-1][g]
    result_list.append(arr[K][n])

for i in result_list:
    print(i)

# tcs = int(input())
# memo = [[0] * 15 for _ in range(15)]
# for tc in range(tcs):
#     r = int(input())
#     c = int(input())

#     def func(r, c):
#         if r == 0 or c == 1:
#             memo[r][c] = c
#             return c

#         if memo[r][c]: return memo[r][c]

#         memo[r][c] = func(r-1, c) + func(r, c-1)
#         return memo[r][c]

#     print(func(r, c))