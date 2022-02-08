#청기 백기
#N개의 깃발 중 1번째 선수는 1의 배수 뒤집기. 두번재는 2의 배수에 해당하는 번호 뒤집
#i번째 선수는 i의 배수의 깃발 뒤집. N번째 선수까지 가면 끝.
#청색이 위로, 백색은 아래로 있음.
#1 2 3 청True 백False
#백 백 백 1번째
#백 청 백 2번째
#백 청 청 3번째
#1일때 전부 뒤집음.
#2로 나눴을 때 홀수이면, 
#2부터
# 백 \청 백 청 백 청 백 청 백 사람 2
# 백 청 \청 청 백 백 백 청 청 사람 3
# 백 청 청 \백 백 백 백 백 청 사람 4 
# N = int(input())

# flag_list =[None] + [True for _ in range(N)] # 1~ N까지이므로 인덱스 0 채워줌.

# for i in range(2, N+1):
#     if N//2 < i:
#         break
#     for j in range(i, N+1):
#         if j%i == 0:
#             if flag_list[j] == True:
#                 flag_list[j] = False
#             elif flag_list[j] == False:
#                 flag_list[j] = True
# count = 0
# for i in range(1, len(flag_list)):
#     if i <= N//2:
#         if flag_list[i] == True:
#             count+=1
#     elif i > N//2:
#         if flag_list[i] == False:
#             count+=1

# print(count) 시간 복잡도 최소화로 깃발을 꽂은 코드. 메모리초과.. 제곱수를 찾는 것이라곤 생각못함.

N = int(input())
# 제곱수 찾기
count = 1 #1도 제곱수
for i in range(2, N+1):
    if i*i > N:
        break
    count += 1
    
print(count)