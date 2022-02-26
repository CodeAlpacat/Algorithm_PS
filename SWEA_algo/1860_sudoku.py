T = int(input())


def row_check(x, list_map): # 속한 행과 스도쿠맵
    one_to_nine = [0 for _ in range(10)] #1~ 9까지
    for i in range(9):
        one_to_nine[list_map[x][i]] += 1

    if max(one_to_nine) > 1:
        return False
    else:
        return True


def col_check(y, list_map): #속한 열 정보, 스도쿠맵
    one_to_nine = [0 for _ in range(10)]  # 1~ 9까지
    for i in range(9):
        one_to_nine[list_map[i][y]] += 1

    if max(one_to_nine) > 1:
        return False
    else:
        return True

def square_check(x, y, list_map):
    one_to_nine = [0 for _ in range(10)]  # 1~ 9까지
    x //= 3
    y //= 3
    for i in range(3):
        for j in range(3):
            one_to_nine[list_map[x*3+i][y*3+j]] += 1

    if max(one_to_nine) > 1:
        return False
    else:
        return True


for tc in range(T):
    li = [list(map(int, input().split())) for _ in range(9)] #스도쿠 맵
    bool_check = True
    for i in range(9):
        for j in range(9):
            if row_check(i, li) and col_check(j, li) and square_check(i, j, li):
                pass
            else:
                bool_check = False
                print(f'#{tc+1} 0')
                break
        if not bool_check:
            break
    else:
        print(f'#{tc+1} 1')