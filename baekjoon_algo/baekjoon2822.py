li = []
for i in range(8):
    N = int(input())
    li.append([i+1, N])

sorted_li = sorted(li, key=lambda x: x[1], reverse=True)

ans = 0
ans_list = []
for i in range(5):
    ans += sorted_li[i][1]
    ans_list.append(sorted_li[i][0])

ans_list.sort()
print(ans)
print(ans_list)