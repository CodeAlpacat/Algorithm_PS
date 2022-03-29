T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    weight = list(map(int, input().split()))
    res = 0
    for i in range(len(weight)):
        min_num = 1000000000
        idx = 0
        flag = False
        for j in range(len(container)):
            if weight[i] >= container[j]:
                if min_num >= weight[i] - container[j]:
                    idx = j
                    min_num = weight[i] - container[j]
                    flag = True
        if len(container) and flag:
            res += container.pop(idx)
        
    
    print(f'#{tc} {res}')