#문자열 반복
import sys

N = int(sys.stdin.readline())
list_result = []
for _ in range(N):
    list_str = ""
    num, str_input = sys.stdin.readline().split()
    for i in range(len(str_input)):
        for j in range(int(num)):
            list_str += (str_input[i])
    list_result.append(list_str)
for i in list_result:
    print(i)
