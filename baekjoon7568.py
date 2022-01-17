#덩치
#몸무게 = x, 키 = y,  덩치 = (x, y)
#덩치의 순위를 비교해 비교 불가 = 같은 순위.
#N = 전체 사람의 수
"""
import collections
N = int(input())

#key값 = 몸무게, value = 키
person_Dict = collections.OrderedDict()
result_list = []

for _ in range(N):
    key, value = map(int, input().split())
    person_Dict[key] = value

#key 와 value 각각 비교해서 비교 불가면 pass, 작다면 +1, 크다면 pass. ex ) A, B, C, D, E 5명의 덩치 비교
# count는 비교 대상이 A에서 B로 옮겨갈 때 초기화
# 2차원 배열로 푸는 문제인데 딕셔너리로 key 값을 몸무게로 놨는데 틀린다. 그 이유는 딕셔너리의 key와 value는 순서가 없어서... OrderedDict를 사용한다.
for key1, value1 in person_Dict.items():
    count = 1
    for key2, value2 in person_Dict.items():
        if key1 < key2 and value1 < value2:
            count += 1

    result_list.append(count)

for i in result_list:
    print(i, end = " ")
"""
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in arr:
  result = 1
  for j in arr:
    if i[0] < j[0] and i[1] < j[1]:
      result += 1
  
  print(result, end = " ")
  