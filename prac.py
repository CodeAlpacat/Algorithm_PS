# import sys
# sys.stdin=open('sample_input.txt')

#중심에서의 거리가 k = 1은 거리 0. k =1, 거리 1, k=3, 거리2, k=4, 거리3
#1 5 13 25 50
# 4 8  12 25

def cost(x): #x는 k의 크기
    cnt = 0
    t = 0
    while t < x:
        cnt += ((2 * t + 1) * 2)
    cnt += (2*x-1)

    return cnt

def check_profit(arr):
    max_pro = -100000000
    
    for i in range(1, len(arr)):
        max_pro = max(max_pro, arr[i] * M - cost(i))
    
    return max_pro


def check_result():
    max_profit = -100000000
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for p in range(N):
                    t = 1
                    list_k = [0] * (2//N+1) #거리가 t인 집의 수
                    while t < (2//N+1):
                        if mat[k][p] == 1 and abs(i-k) + abs(j-p) == t:
                            list_k[t] += 1
                        t += 1
                    max_profit = max(max_profit, check_profit(list_k))
    return max_profit
            
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(check_result())