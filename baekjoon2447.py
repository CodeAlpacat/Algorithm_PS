#별 찍기 - 10 (재귀)
#사실 못풀겠음 이거

def draw_star(n) :
    global Map
    # 2차원 global 변수
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        # 첫 번째 행의 1~3열과 세 번째 행의 1~3열은
        # [1] (별이 있다는 뜻) 이 3개 들어간 형태
        # [1] * 3 을 해줄 경우 [1, 1, 1]의 행이 만들어짐!
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(n//3)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

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