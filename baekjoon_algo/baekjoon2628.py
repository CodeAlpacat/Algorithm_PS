#종이자르기

width, height = map(int, input().split())
width_cut_list = [0, height] # 자른 가로 점선들을 저장할 리스트
height_cut_list = [0, width] # 자른 세로 점선들을 저장할 리스트

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    if A == 0:
        width_cut_list.append(B)
    elif A == 1:
        height_cut_list.append(B)
    else:
        print("잘못입력하신듯?")
        break

width_cut_list.sort()
height_cut_list.sort() # 정렬

result_width = 0
for i in range(len(width_cut_list)-1):
    if width_cut_list[i+1] - width_cut_list[i] >= result_width:
        result_width = width_cut_list[i+1] - width_cut_list[i]

result_height = 0
for i in range(len(height_cut_list)-1):
    if height_cut_list[i+1] - height_cut_list[i] >= result_height:
        result_height = height_cut_list[i+1] - height_cut_list[i]

print(result_height*result_width)
