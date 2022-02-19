#용액
import sys
N = int(input())
li = list(map(int, input().split()))
s = 0
e = N-1
idx_s = 0
idx_e = 0
min_mix = sys.maxsize
while s < e:
    sum_liq = li[s] + li[e]

    if abs(sum_liq) < min_mix:
        idx_s = s
        idx_e = e
        min_mix = abs(sum_liq)

    if sum_liq > 0:
        e -= 1
    elif sum_liq < 0:
        s += 1
    else:
        break

print(li[idx_s], li[idx_e])
#-99 -2 -1 4 98
#     s
#          e