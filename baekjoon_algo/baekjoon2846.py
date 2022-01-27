#오르막길
#오르막 내리막 평지 일정 거리마다 높이 측정
#가장 큰 오르막길의 크기
#오르막길은 크기가 증가하는 부분 수열
#적어도 2이상 차이나야 오르막
N = int(input())
start = 0 #오르막 시작
up_list = list(map(int, input().split()))

result_list = []#오르막길들이 들어갈 리스트

for i in range(1, len(up_list)):
    if up_list[i] > up_list[i-1]:
            start += up_list[i] - up_list[i-1] # 오르막의 크기.
            if i ==len(up_list) - 1:
                result_list.append(start)
    else:
        result_list.append(start)
        start = 0

print(max(result_list))