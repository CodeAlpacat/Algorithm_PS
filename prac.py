from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq


def compose_members(cur, total, cnt):
    global ans

    if total_stats - total * 2 < 0 or cnt > N//2: # 만약 선수 능력치나 선수 수의 밸런스가 깨진다면, False
        return

    if total_stats == (total * 2) and cnt == N//2: #현재 고른 선수들의 능력치의 합 * 2 == 총 능력치이고  and  현재 고른 선수들의 수 == 전체 선수 수의 절반
        ans = True
        return

    if cur > N: #리스트 범위를 벗어나는 경우 False
        return

    if cur == N: #선수 분배를 완료하지 못하고 리스트의 끝에 도달하는 경우 False
        return


    compose_members(cur + 1, total + players[cur], cnt + 1) # 선수를 골라서 팀에 능력치를 더해줌
    compose_members(cur + 1, total, cnt) #선수를 고르지 않음


#사람 수(N) => 10~ 16명 제한
T = int(input())
list_res = []
for tc in range(T):
    N = int(input())
    players = list(map(int, input().split()))
    total_stats = sum(players) #선수들의 총 능력치
    ans = False #디폴트로 False로 아직 선수들의 분배가 이루어지지 않았음.
    compose_members(0, 0, 0)

    list_res.append(ans)

for i in range(len(list_res)):
    print(f'#{i+1} {list_res[i]}')




#########################################

# def compose_members(cur, total, cnt):

#     if total_stats - total < 0 or cnt > N//2:
#         return False

#     if total_stats == (total * 2) and cnt == N//2: #현재 고른 선수들의 능력치의 합 * 2가 총 능력치와 같고 선수의 수도 절반을 차지해야함
#         return True

#     if cur > N:
#         return False

#     if cur == N: #선수들 리스트를 벗어나면 리턴
#         return False

#     if memo[cur][total][cnt] != -1:
#         return memo[cur][total][cnt]

#     memo[cur][total][cnt] = (compose_members(cur + 1, total + players[cur], cnt + 1)) or compose_members(cur + 1, total, cnt)
#     return memo[cur][total][cnt]


# #사람 수(N) => 10~ 16명 제한
# #
# T = int(input())

# for tc in range(T):
#     N = int(input())
#     players = list(map(int, input().split()))
#     total_stats = sum(players)
#     memo = [[[-1] * N for _ in range(total_stats)] for _ in range(N)]

#     print(compose_members(0, 0, 0))


