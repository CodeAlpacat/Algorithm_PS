#View
list_result = []

for x in range(10):
    count = 0
    num = int(input())
    view = list(map(int, input().split()))
    for i in range(2, num-2): #첫 두자리와 끝 두자리는 비어있음
        if view[i] > view[i-1] and view[i] > view[i-2] and view[i] > view[i+1] and view[i] > view[i+2]:
            count += view[i] - max(view[i-1], view[i-2], view[i+1], view[i+2])
        else:
            continue
    list_result.append(count)

for i in range(10):
    print(f'#{i+1} {list_result[i]}')