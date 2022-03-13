#연산자 끼워넣기
N = int(input())
li_num = list(map(int, input().split()))
li_op = list(map(int, input().split()))
max_ans = -1000000000
min_ans = 1000000000
def recur(cur, total, p, m, mu, div):
    global max_ans
    global min_ans

    if cur == N:
        max_ans = max(max_ans, total)
        min_ans = min(min_ans, total)
        return
    
    if p > 0:
        recur(cur + 1, total + li_num[cur], p - 1, m, mu, div)
    if m > 0:
        recur(cur + 1, total - li_num[cur], p, m - 1, mu, div)
    if mu > 0:
        recur(cur + 1, total * li_num[cur], p, m, mu - 1, div)
    if div > 0:
        recur(cur + 1, int(total / li_num[cur]), p, m, mu, div - 1)
        

recur(1, li_num[0], li_op[0], li_op[1], li_op[2], li_op[3] )

print(max_ans)
print(min_ans)