T = int(input())


list_result = []
for x in range(T):
    N = int(input())
    card = int(input())
    list_card = [0] * 10

    while card > 0:
        list_card[card % 10] += 1
        card //= 10

    max = list_card[0]
    index = 0
    for i in range(len(list_card)):
        if max <= list_card[i]:
            index = i
            max = list_card[i]
    list_result.append([index, max])
for i in range(len(list_result)):
    print(f'#{i+1} {list_result[i][0]} {list_result[i][1]}')