carved_str = input()

N = int(input())

cnt = 0
for tc in range(N):
    slot = list(input())
    for i in range(10):
        if ''.join(slot[:len(carved_str)]) == carved_str:
            cnt += 1
            break
        slot.append(slot.pop(0))
           
print(cnt)