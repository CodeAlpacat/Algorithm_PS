
import numbers


sublist = numbers[:50]

def mergeSort(list):
	size = len(list)
	if size <= 1: return list

	mid = len(list) // 2
	left = mergeSort(list[:mid])
	right = mergeSort(list[mid:])
	merged = merge(left, right) # 각 재귀의 끝에서 합병해주는 역할.
	return merged

def merge(list1, list2):
	merged = []
    #슬라이싱 예제1은 l과 h 변수를 0으로 초기화하고 1씩올렸고, 이 예제2에서는 pop으로 리스트가 빌 때까지 반복한다.
	while len(list1) > 0 and len(list2) > 0:
		if list1[0] <= list2[0]:
			merged.append(list1.pop(0)) #왼쪽끝 인덱스를 merged 리스트에 추가하고 list1에서 빼냄.
		else:
			merged.append(list2.pop(0)) #반대로 비교했을때 오른쪽 수가 크면 오른쪽먼저 넣음.
#while문이 끝나고 남은 값들은 다시 merged에 이어줌.
	if len(list1) > 0:
		merged += list1
	if len(list2) > 0:
		merged += list2

	return merged


sorted = mergeSort(sublist)
print (sorted)