T = int(input())

def elec_station(K, N, M, station):
    count = 0  # 충전 횟수
    point = 0
    for i in range(len(station)):

        if point > i: #충전을 한 지점부터 다시 시작
            continue
        for j in range(1, len(station)):
            if station[j] - station[j-1] > K:
                return 0

        for j in range(i, len(station)):
            if i != j and station[j] - station[i] > K:  # 만약 갈 수 있는 거리보다 크면 그 전 정류장에서 충전
                count += 1  # 충전
                point = j - 1 # 인덱스에러 조심. i가 point일 때까지 continue 0 0 일때 위험한데 0일 땐 if문 못들어옴.
                break
            elif i != j and station[j] - station[i] == K:
                if station[j] == N:
                    break
                else:
                    count += 1
                    point = j
                break
    return count

result_list = []
for x in range(T):
    K, N, M = map(int, input().split())
    station = [0] + list(map(int, input().split())) + [N]
    # 1 3 5 7 9
    e = elec_station(K, N, M, station)
    result_list.append(e)

for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')

