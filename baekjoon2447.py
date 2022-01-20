#별 찍기 - 10 (재귀)
#사실 못풀겠음 이거

def draw_star(n) :
    global Map
    # 2차원 global 변수
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        # 1행 3행은 모두 1이 들어감
        Map[1][:3] = [1, 0, 1] # 2행만 가운데 0이 들어감.
        return

    a = n//3
    draw_star(n//3) #재귀 시작
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어
                #n = 27일때, a =9, i는 2까지 증가하고 i가 1일때, k가 사각형안의 별들을 1씩 증가하며 채워넣음. 열도 0부터 j까지 열 별로 채워넣음.

N = int(input())      

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()