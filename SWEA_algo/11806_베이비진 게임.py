def check(li):
    count_arr = [0] * 10
    for i in range(len(li)):
        count_arr[li[i]] += 1

    for i in range(len(count_arr)):
        if count_arr[i] >= 3:
            return True
        if i < len(count_arr) - 2:
            if count_arr[i] and count_arr[i+1] and count_arr[i+2]:
                return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr1 = []
    arr2 = []
    ans = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            arr1.append(arr[i])
            if len(arr1) >= 3:
                if check(arr1):
                    ans = 1
                    break
            #플레이어1카드
        else:
            arr2.append(arr[i])
            if len(arr2) >= 3:
                if check(arr2):
                    ans = 2
                    break
    else:
        ans = 0
            #플레이어2카드
    
    print(f'#{tc} {ans}')