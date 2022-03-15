#치킨 배달 (하드코어)
def find(cur, x, y):
    global ans
    if cur == m:
        r = []
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 100:
                    r.append([i,j])
        res = far(r, house)

        if ans > sum(res):
            ans = sum(res)
        return
    
    for i in range(x, n):
        if i == x:
            for j in range(y, n):
                if arr[i][j] == 2:
                    arr[i][j] = 100
                    find(cur+1, i, j+1)
                    arr[i][j] = 2
        else:
            for j in range(n):
                if arr[i][j] == 2:
                    arr[i][j] = 100
                    find(cur+1, i, j+1)
                    arr[i][j] = 2

def far(c, h):
    res = []
    for i in h: #치킨집과 선정된 치킨집까지의 거리 중 최소값인 치킨거리
        min_num = 100000000
        for j in c:
            fars = abs(i[0]-j[0]) + abs(i[1]-j[1]) 
            min_num = min(min_num, fars)
        res.append(min_num)
    return res

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 99999
house = []
for i in range(n):
    for j in range(n):
        if(arr[i][j] == 1):
            house.append([i,j])

find(0,0,0)
print(ans)

