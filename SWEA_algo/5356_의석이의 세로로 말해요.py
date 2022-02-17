T = int(input())

for x in range(T):
    li = []
    cnt = 0 #최장 길이 문자열 찾기
    for i in range(5):
        str_toy = list(input())
        li.append(str_toy)
        if cnt < len(str_toy):
            cnt = len(str_toy)
    
    for i in range(5):
        if len(li[i]) < cnt: #abc 5
            for j in range(cnt-len(li[i])):
                li[i].append(10) #10은 입력 받지 않을 숫자
    str_res =''
    for i in range(cnt):
        for j in range(5):
            if li[j][i] == 10:
                continue
            else:
                str_res += li[j][i]
    
    print(f'#{x+1} {str_res}')