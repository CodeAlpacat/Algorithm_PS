T = int(input())

for i in range(T): # 3
    N = int(input()) # 0 일때 5 들어감.
    
    case_split = list(map(int, input().split()))
    result = 0
    for j in range(len(case_split) - 1):
        if result <= case_split[j] + case_split[j+1]:
            result = case_split[j] + case_split[j+1]
        else:
            continue
                
    print(f'#{i+1} {result}')