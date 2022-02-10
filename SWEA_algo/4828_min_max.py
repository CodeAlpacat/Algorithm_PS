T = int(input())
list_val = []
for x in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    max = num[0]
    min = num[0]
    for i in range(len(num)):
        if max < num[i]:
            max = num[i]

        if min > num[i]:
            min = num[i]
    list_val.append(max-min)
for i in range(len(list_val)):
    print(f'#{i+1} {list_val[i]}')