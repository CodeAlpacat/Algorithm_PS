N = int(input())
mat = list(map(int, input().split()))

def check(lis):
    if (lis[0] / lis[1]) == lis[2]:
        return True
    else:
        return False
li = []
def recur(cur, cnt):
    global res
    if cur == N:
        return

    if len(li) == 3:
        res += check(li)
        return  

    li.append(mat[cur])
    recur(cur + 1, cnt + 1)
    li.pop()
    recur(cur + 1, cnt)
        

res = 0
recur(0, 0)
print(res)








S = list(input())
set_S = set(S)

cnt_upper = 0
cnt_lower = 0
for i in S:
    if 'a' <= i <= 'z':
        cnt_lower += 1
    elif 'A' <= i <= 'Z':
        cnt_upper += 1

if len(S) != len(set_S):
    print('No')
else:
    if cnt_lower == 0 or cnt_upper == 0:
        print('No')
    else:
        print('Yes')





a, b, c, d, e, f, X = map(int, input().split())

Xt = X
ans = 0
cnt = 0
while Xt:
    if cnt % a == 0 and cnt != 0:
        Xt -= c
        if Xt <= 0:
            break
    ans += b
    cnt += 1
    Xt -= 1

Xy = X
cnt_a = 0
ans_a = 0
while Xy:
    if cnt_a % d == 0 and cnt_a != 0:
        Xy -= f
        if Xy <= 0:
            break
    ans_a += e
    cnt_a += 1
    Xy -= 1
    
if ans > ans_a:
    print('Takahashi')
elif ans < ans_a:
    print('Aoki')
else:
    print('Draw')
