#N 임한수 김지민의 번호
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

#2 4 6 8 10 12 14 16
#1 2 3 4 5  6  7  8

N, A, B = map(int, input().split())
cnt = 0
while abs(A - B) and A and B:
    
    if A % 2 == 1:
        A = (A+1) // 2
    else:
        A //= 2
    
    if B % 2 == 1:
        B = (B+1) // 2
    else:
        B //= 2

    cnt += 1
if cnt == N:
    print(-1)
else:
    print(cnt)

#12
#6
#4
#2
#1