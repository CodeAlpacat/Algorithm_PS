T = int(input())


#가로로 줄긋기
def garo_cut(arr, N):
    total = 0
    for i in arr:
        for j in i:
            total += j

    max_min = total
    for i in range(N-1):
        for j in range(N-1):
            a = 0# arr[0:i+1][0:j+1] # 다 더하는거 구현
            for k in range(0, i+1):
                for p in range(0, j+1):
                    a += arr[k][p]

            b = 0# arr[0:i+1][j+1:N]
            for k in range(0, i+1):
                for p in range(j+1, N):
                    b += arr[k][p]

            c = total - (a + b) # a+b는 위쪽 전체 합 c = 아래 전체합
            
            if max_min > max(a, b, c) - min(a, b, c):
                max_min = max(a, b, c) - min(a, b, c)
            
            d = 0#arr[i+1:N][0:j+1] #이차원 리스트 합
            for k in range(i+1, N):
                for p in range(0, j+1):
                    d += arr[k][p]
            e = 0# arr[i+1:N][j+1:N]
            for k in range(i+1, N):
                for p in range(j+1, N):
                    e += arr[k][p]
            if max_min > max(a+b, d, e) - min(a+b, d, e):
                max_min = max(a+b, d, e) - min(a+b, d, e)
    return max_min

for x in range(T):
    N = int(input())
    farm = [list(map(int, input().split())) for i in range(N)]
    new_farm = list(map(list, zip(*farm))) #가로축 세로축 역전
    farm_sum = garo_cut(farm, N)
    farm_sum_rev = garo_cut(new_farm, N)
    if farm_sum < farm_sum_rev:
        print(farm_sum)
    else:
        print(farm_sum_rev)
        
    
    #세로로 줄긋기

#2 3 2 2 1
#---------
#3 1 1 1 3
#3 2 3 1 3
#1 1 3 2 1
#2 2 2 1 1
#가로선 윗줄긋기
#가로 1 세로 1 => 위쪽 아래쪽에 세로로 줄그을 경우의 수
#tc1 => 1행~ 5행의 합, 0행 0열, 0행 1~4열
#tc2 => '', 0행 0~ 1열, 2~ 4열
#...
#가로선 아랫줄긋기

#세로
#2 | 3 2 2 1
#3 | 1 1 1 3
#3 | 2 3 1 3
#1 | 1 3 2 1
#2 | 2 2 1 1