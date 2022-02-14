T = int(input())
result_list = []
for x in range(T):
    N, K = map(int, input().split())
    li = list(map(int, input().split()))
    count = 0
    for i in range(1 << N): # 모든 경우의 수 탐색
        sum_n = 0
        for j in range(len(li)): #모든 경우의 수에서 각 수의 이진수가 j의
            if i & (1 << j):
                sum_n += li[j] # i의 비트 중 j의 비트에 해당하면 누적합.
        if sum_n == K:
            count += 1
    
    result_list.append(count)

for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')