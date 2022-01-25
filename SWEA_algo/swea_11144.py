T = int(input())

for i in range(T):
    list_num = list(map(int, input().split()))
    if 5 <= len(list_num) <= 20:
        print(f'#{i+1}', len(list_num), list_num[-1], sep =' ')
    else:
        print("입력이 5개 미만 or 20개 초과인데?")