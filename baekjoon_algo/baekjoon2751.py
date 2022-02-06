import sys
N = int(sys.stdin.readline())

arr = [False for _ in range(2000001)] # 최대값이 1000000이므로 범위 전체를 포함하는 범위

for _ in range(N):
    arr[int(sys.stdin.readline()) + 1000000] = True

result_list = []
for i in range(len(arr)):
    if arr[i]:
        result_list.append(i-1000000)

for i in result_list:
    sys.stdout.write(str(i)+'\n')
