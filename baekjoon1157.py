#단어 공부
#중복이 많은 문자가 무엇인지 판단하는 문제
"""
시간초과 ~ 입니다~
import sys

N = sys.stdin.readline()
# 대문자로 변환
new_str =""
for i in N:
    if ord(i)>96:
        new_str += chr(ord(i)-32)
    else:
        new_str += i

max_num = 0
result = ''

for i in range(len(N)):
    if max_num < new_str.count(new_str[i]):
        max_num = new_str.count(new_str[i])
        result = new_str[i]
    elif max_num == new_str.count(new_str[i]) and result != new_str[i]:
        result = '?'
    else:
        continue
print(result)
"""

# sys.stdin.readline()으로 입력받으면 오답..?
import sys
N = input().lower()
unique_N = list(set(N))

cnt = []
for i in unique_N:
    count = N.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >=2:
    print('?')
else:
    max_index = cnt.index(max(cnt))
    print(unique_N[max_index].upper())