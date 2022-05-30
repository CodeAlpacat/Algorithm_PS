from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq


def catch_robot(cur, A_total, B_total):
    global ans

    if cur > N:
        return

    if cur == N:
        ans = min(cur, ans)
        #여기서 B_total과 A_total을 비교
        return
    
    if A_total >= B_total:
        ans = min(cur, ans) #A가 B를 따라잡았을 때, 날짜의 최솟값(빨리 따라잡을 수록 좋다)
        return

    catch_robot(cur + A_list[cur][0], A_total + A_list[cur][1], sum(B_list[0:cur+1]) + start_dist) # 선택하면 뛰어서 ?KM가고 ?시간 만큼 쉬어준다.
    catch_robot(cur + 1, A_total + 1, sum(B_list[0:cur+1])+start_dist) #굳이 선택안하고 걷더라도 1km씩은 쉬지 않고 걷는다.

T = int(input()) #테스트 케이스 개수

for tc in range(T):
    N = int(input()) #달릴 수 있는 총 시간
    A_list = [] # [[달리고 쉬어줄 시간, 달릴 수 있는 거리], ....]
    for i in range(N):
        single_case = list(map(int, input().split())) # A의 각 케이스
        A_list.append(single_case)
    
    B_list = list(map(int, input().split())) #쉬지 않고 꾸준히 달리는 로봇
    start_dist = int(input()) #시작부터 벌어져있는 거리

    ans = 0xffffff
    catch_robot(0, 0, start_dist)
    print(ans)

# 1
# 3
# 0 3 #쉬어줘야하는 일수(1일 경우는 1일만 증가하므로 안쉬어주는거나 다름없음)
# 1 5
# 2 7
# 1 2 3
# 5

#  0  1      2        3       4
#  0  3km    8km      8       8
#  5  6km    8km     11km