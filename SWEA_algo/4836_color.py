T = int(input())

for x in range(T):
    N = int(input())
    draw = [[0 for i in range(10)] for j in range(10)]
    count = 0
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(a[0], a[2]+1):
            for k in range(a[1], a[3]+1):
                if draw[j][k] != a[4] and draw[j][k] != 0:
                    count += 1 #보라색 10으로 놓자
                    draw[j][k] = 10
                else:
                    draw[j][k] = a[4]

    print(f'#{x+1} {count}')