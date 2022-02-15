#부분집합의 합
T = int(input())

for x in range(T):
    N, K = map(int, input().split()) # 집합 원소의 개수, 합
    A = [i for i in range(1, 13)] #1~ 12 까지인 집합 A
    ans = 0
    for i in range(1 << len(A)):
        cnt = 0
        sum_a = 0
        for j in range(len(A)):
            if i & (1 << j):
                cnt += 1
                sum_a += A[j]
        if cnt == N and sum_a == K:
            ans += 1
    print(f'#{x+1} {ans}')
