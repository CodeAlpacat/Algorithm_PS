#암호 만들기
L, C = map(int, input().split())
secret_num = list(input().split())
secret_num.sort()
alpha = []
moeum = ['a', 'e', 'i', 'o', 'u']
def recur(cur, cnt):

    if cnt > L:
        return    

    if cnt == L:
        cnt = 0
        cnt_other = 0
        for i in range(len(alpha)):
            if alpha[i] in moeum:
                cnt += 1
            elif alpha[i] not in moeum:
                cnt_other += 1
        if cnt > 0 and cnt_other > 1:
            print(''.join(alpha))
            return
        else:
            return

    if cur == C:
        return

    alpha.append(secret_num[cur])
    recur(cur + 1, cnt + 1)
    alpha.pop()
    recur(cur + 1, cnt)

recur(0, 0)