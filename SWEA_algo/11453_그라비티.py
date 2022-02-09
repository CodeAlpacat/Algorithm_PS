N = int(input())

for x in range(N):
    box = list(map(int, input().split()))
    result = 0
    for i in range(len(box)):
        count = 0
        for j in range(i, len(box)):
            if i != j and box[i] > box[j]:
                count += 1
        if result < count:
            result = count
    print(f'#{x+1} {result}')