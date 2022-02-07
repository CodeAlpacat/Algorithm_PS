#최대 GCD
N = int(input())

list_result = []
for _ in range(N):
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True) # 앞의 수가 뒤보다 커야 유클리드 호재법을 사용가능
    list_GCD= []
    for i in range(len(num_list)): # 40 30 20 10
        for j in range(i, len(num_list)): # 40, 40 30 20 10
            if i != j:
                x, y = num_list[i], num_list[j] #리스트의 수가 바뀌어버리면 다음 반복때 망가짐.
                while x%y != 0:
                    x, y = y, x%y
                list_GCD.append(y)
    list_result.append(max(list_GCD))

for i in list_result:
    print(i)