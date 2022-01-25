#테스트 케이스 T
T = int(input()) 
#높이H 와 너비W를 입력받아 사각형 형태로 숫자를 출력
for i in range(1, T+1):
    H, W = map(int, input().split())
    print(f'#{i}') # 테스트 케이스의 순서
    
    for j in range(1, H+1):
        for k in range(j, W*H+1, H):
            print(k, end = ' ')
        print()