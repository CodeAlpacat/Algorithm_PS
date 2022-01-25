#테스트 케이스 T
T = int(input()) 
#높이H 와 너비W를 입력받아 사각형 형태로 숫자를 출력
#숫자는 지그재그로 증가
for i in range(1, T+1):
    H, W = map(int, input().split())
    num_saved = 0 #현재 숫자를 저장해줄 변수
    
    print(f'#{i}') # 테스트 케이스의 순서
    for k in range(1, H+1):
        if k % 2 == 1: #홀수 줄 #이전 줄 다음 숫자부터 시작
            for j in range(num_saved+1, num_saved+W+1):
                print(j, end = ' ')
            print()
            num_saved += W
        else: # 짝수줄 # 
            for j in range(num_saved+W, num_saved, -1):
                print(j, end = ' ')
            print()
            num_saved += W
    