#모험가 길드
#모험가 N명 입력. N명을 대상으로 '공포도'를 측정. '공포도'가 높으면 위험 상황에서 대처능력이 떨어짐.
#공포도가 X인 모험가는 X명 이상으로 구성한 그룹에 참여해야 함.
#최대 몇 개의 그룹을 만들 수 있을까?
#모험가 N명과 N이하의 자연수를 두 번째 줄에 각 모험가의 공포도의 값을 공백 단위로 입력.

#풀이 -> 공포도가 높을수록 사람을 많이 요구하므로 공포도가 높은 사람부터 계산 (그리디 알고리즘)
'''
N = int(input())

num_fear = list(map(int, input().split()))#N명 만큼 모험가의 공포도를 입력받음

sorted_fear = sorted(num_fear) # 오름차순 정렬
people_left = N #people_left가 0이 되거나 그 이하면 그룹을 만들 수 없음.
count = 0
for i in sorted_fear:
    if people_left <=0:
        print(count-1)
        break
    else:
        people_left = people_left - i # i는 공포도이므로 사람 수만큼 빼준다.
        count +=1 # 그룹 1개 생성. 
'''

N = int(input())

data = list(map(int, input().split()))
data.sort()

result = 0 #그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 순으로 확인하며, 공포도보다 모험가 수가 같거나 많다면, 그룹의 수를 +1하고 현재 그룹원을 0으로 초기화.
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

