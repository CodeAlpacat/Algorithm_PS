
# A = [1, 2, 3]

# bit = [0] * 3

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for p in range(3):
#                 if bit[p]:
#                     print(A[p], end = ' ')
#             print()

#--------------------------------

arr = [3, 6, 7, 1, 5, 4] #2^0, 2^2, 2^3, 2^4, 2^5, 2^6
#1, 10, 100, 1000, 10000, 100000

n = len(arr)

for i in range(1<<n): # 부분 집합의 개수만큼 반복 63개 전부(공백 제외)
    for j in range(n): #원소의 수만큼 비트 비교
        if i & (1<<j): # i의 j번 비트가 1인경우
            print(arr[j], end=', ')
    print()
print()