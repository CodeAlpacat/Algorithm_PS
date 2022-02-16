T = int(input())
res_li = []
for x in range(T):
    str1 = list(set(input()))
    str2 = input()
    max_cnt = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        
        if max_cnt < cnt:
            max_cnt = cnt
    
    res_li.append(max_cnt)

for i in range(len(res_li)):
    print(f'#{i+1} {res_li[i]}')

        
        