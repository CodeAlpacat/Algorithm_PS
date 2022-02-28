def check(val):
    for i in range(len(bingo_map)):
        for j in range(len(bingo_map)): # 22라면 4, 0
            if val == bingo_map[i][j]:
                record_li[i][j] = 1
                row_check(i)
                col_check(j)
                if i == j:
                    cross_check()
                if j == 4-i:
                    rev_cross_check()
                if sum(bingo) >= 3:
                    return True

    else:
        return False

def row_check(x):
    cnt = 0
    for i in range(5):
        if record_li[x][i] == 1:
            cnt += 1
    if cnt == 5 and not visited_row[x]:
        bingo[0] += 1
        visited_row[x] = True
        return
    else:
        return

def col_check(y):
    cnt = 0
    for i in range(5):
        if record_li[i][y] == 1:
            cnt += 1
    if cnt == 5 and not visited_col[y]:
        bingo[1] += 1
        visited_col[y] = True
        return
    else:
        return

def cross_check():
    cnt = 0
    for i in range(5):
        if record_li[i][i] == 1:
            cnt += 1
    if cnt == 5:
        bingo[2] = 1
        return
    else:
        return

def rev_cross_check():
    cnt = 0
    for i in range(5):
        if record_li[i][4-i] == 1:
            cnt += 1
    if cnt == 5:
        bingo[3] = 1
        return
    else:
        return


visited_row =[False] * 5
visited_col =[False] * 5
bingo = [0, 0, 0, 0] #각각 가로 세로 대각, 역대각. 총 합이 3이상이면 성공
bingo_map = [list(map(int, input().split())) for _ in range(5)]
li_call = [list(map(int, input().split())) for _ in range(5)]
record_li = [[0] * 5 for _ in range(5)]
count = 0
switch = False
for i in range(len(li_call)):
    for j in range(len(li_call)):
        count+=1
        if check(li_call[i][j]):
            print(count)
            switch = True
            break
    if switch:
        break