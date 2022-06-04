from collections import deque
import math
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq
a = 'A+C'
b = 'DEF'

#fr ra an nc ce 
#fr re en nc ch
#개수 같으면 합 교 둘다 더해줌
#개수가 더 많으면 합, 적으면 교에 들어감
#
c = 'aa1+aa2'
d = 'AAAA12'
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = []
    str2_list = []
    #문자열 나눠주기
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        # if 97 <= ord(str2[i]) < 123 and 97 <= ord(str2[i+1]) < 123:
        if str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2])

    union_sum = 0
    intersect_sum = 0
    i = 0
    done_list = []
    while len(str1_list) > i:
        a = 0
        b = 0
        if str1_list[i] not in done_list:
            for j in range(len(str1_list)):
                if str1_list[i] == str1_list[j]:
                    a += 1
            for j in range(len(str2_list)):
                if str1_list[i] == str2_list[j]:
                    b += 1
            

            if a == b:
                union_sum += a
                intersect_sum += a
            else:
                union_sum += max(a, b)
                intersect_sum += min(a, b)
        
            done_list.append(str1_list[i])
        i += 1

    cnt_leftover = 0
    for i in range(len(str2_list)):
        if str2_list[i] in done_list:
            continue
        cnt_leftover += 1

    if not intersect_sum and not union_sum and cnt_leftover:
        return 0
    elif intersect_sum + union_sum == 0:
        return 65536
    else:
        answer = intersect_sum / (union_sum + cnt_leftover) * 65536
        answer = math.floor(answer)
    return answer

print(solution(a, b))