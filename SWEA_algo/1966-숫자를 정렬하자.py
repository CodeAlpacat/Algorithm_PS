t = int(input())
def counting_sort(arr, K): #K는 범위의 최대값인 50이다.
    c = [0] * K
    sorted_arr = [0] * len(arr)

    for i in range(len(arr)):
        c[arr[i]] += 1

    for i in range(1, K):
        c[i] += c[i-1]

    for i in range(len(arr)):
        sorted_arr[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1

    return sorted_arr

result_list = []
for x in range(t):
    N = int(input())
    num_list = list(map(int, input().split()))
    result_list.append(counting_sort(num_list, 50))

for i in range(len(result_list)):
    print(f'#{i + 1}', end= ' ')
    for j in result_list[i]:
        print(j, end = ' ')
    print()