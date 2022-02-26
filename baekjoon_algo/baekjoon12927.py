def change(switch):
    if switch == 'Y':
        return 'N'
    else:
        return 'Y'

li = [0] + list(input())
cnt = 0
for i in range(1, len(li)):
    if li[i] == 'Y':
        for j in range(1, len(li)):
            if j % i == 0:
                li[j] = change(li[j])
        cnt += 1
    else:
        continue

print(cnt)