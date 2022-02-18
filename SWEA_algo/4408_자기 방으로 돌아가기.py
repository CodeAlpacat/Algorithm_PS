T = int(input())

for x in range(T):
    N = int(input())
    li = [0] * 401 # 400개의 방

    for i in range(N):
        A, B = map(int, input().split())
        if A % 2 == 1:
            A += 1
        if B % 2 == 1:
            B += 1 #홀수 +1 = 짝수인덱스와 같은 줄
        if A <= B:
            for j in range(A, B+1):
                li[j] += 1
        else:
            for j in range(B, A+1): #뒤 쪽에서 앞 복도로 가는 애들
                li[j] += 1
        
    print(f'#{x+1} {max(li)}')


    #10 20
    #19 30
    #30 40
    #50 60
    #70 80
    #90 100

#1 3 5 7  9 11 13 15 17 19 21 23 25 27
#  c      c
#  b
#a a   b
#2 4 6 8 10 12 14 16 18 20 22 24 26 28

#1 2 -> 