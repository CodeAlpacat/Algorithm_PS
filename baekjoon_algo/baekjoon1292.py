#쉽게 푸는 문제
#1 2 2 3 3 3 4 4 4 4
#1 2 3 4 5 6 7 8 9 10
#6개의 인덱스 5까지 1+2+3 -1 임. 인덱스 1+2+3+4 -1은 10개째 인덱스
#1~N까지의 합이 인덱스이면, 숫자 N의 마지막 숫자임.
#1*1 + 2*2 + 3*3 + 4*4 = 값
# 1+2+3+4 = 인덱스
#1*1 + 2*2 .. i*j
#처음 자릿수까지만 올라감. j가 i에 도달하면 j의 값을 count에 저장. 입력과 비교할 용도
#로직꼬임   ㅋㅋㅋㅋㅋㅋㅋㅋㅋ 무지성 코딩
A, B = input().split()
A, B = int(A), int(B)


def calc_B(X):
    sum_A = 0
    count_A = 0
    i = 1
    while True:
        for j in range(1, i+1):
            if count_A + j == X: #A=3, 1차시 count = 1, 2차 count =
                sum_A += i
                count_A += j
                return sum_A
            else:
                sum_A += i
                continue
        if X > count_A:
            count_A += i
            i += 1
        if X == count_A:
            return sum_A
def calc_A(X):
    sum_A = 0
    count_A = 0
    i = 1
    while True:
        for j in range(1, i+1):
            if count_A + j == X: #A=3, 1차시 count = 1, 2차 count =
                count_A += j
                return sum_A
            else:
                sum_A += i
                continue
        if X > count_A:
            count_A += i
            i += 1
        if X == count_A:
            return sum_A
print(calc_B(B) - calc_A(A))
#1 2 2 3 3 3 4