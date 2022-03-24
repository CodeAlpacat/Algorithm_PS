T = int(input())

secret_code = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

def find_column_code():
    for i in range(M):
        for j in range(N):
            if int(secret_table[i][j]):
                return i #탐색할 x좌표 return

def find_start(x_num):
    arr_possible = [] #가능성있는 시작 좌표를 넣을 배열
    for i in range(M-56): # 56자 직전까지가 시작점
        code_start = ''
        for j in range(i, i+7):
            code_start += secret_table[x_num][j]
        for j in secret_code:
            if code_start == j:
                arr_possible.append(i) # y좌표 return
        else:
            continue
    return arr_possible

def check(x, y):
    code_ans = ''
    for i in range(y, y + 50, 7): # 0 7 14 21 28 35 42 49 총 8지점
        str_code = ''
        for j in range(i, i+7):
            str_code += secret_table[x][j]
        if str_code  not in secret_code:
            continue
        code_ans += secret_code[str_code]

        if len(code_ans) == 8:
            return code_ans
    return False

for tc in range(T):
    N, M = map(int, input().split())
    secret_table = []
    for i in range(N):
        secret_table.append(input())
    #시작 x, y좌표
    x = find_column_code() #x좌표
    y_arr = find_start(x) #시작 y좌표 리스트
    res = 0
    for i in y_arr:
        code_ans = check(x, i)
        if code_ans != False:
            res = (int(code_ans[0]) + int(code_ans[2]) + int(code_ans[4]) + int(code_ans[6]))*3 + int(code_ans[1]) + int(code_ans[3]) + int(code_ans[5]) + int(code_ans[7])
            if res % 10 == 0:
                ans = list(map(int, list(code_ans)))
                print(f'#{tc+1} {sum(ans)}')
            else:
                print(f'#{tc+1} {0}')