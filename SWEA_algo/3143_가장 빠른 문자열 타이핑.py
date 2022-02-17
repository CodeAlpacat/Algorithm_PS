T = int(input())

for x in range(T):
    A, B = input().split()
    idx = 0
    cnt = 0
    while idx <= len(A)-len(B)+1:
        if A[idx:idx+len(B)] == B: #슬라이싱한게 B와 같다면
           cnt += 1
           idx += len(B) #asakusa idx=1 -> idx = 3
        else:
            cnt += 1 #일반 타이핑
            idx += 1
    
    if idx != len(A): #인덱스가 A의 길이가아니면 len(A)-len(B)+1에서 다 못끝냄.
        for i in range(idx, len(A)):
            cnt += 1
    #인덱스 A될 때까지 count

    print(f'#{x+1} {cnt}')