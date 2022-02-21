#반복문자 지우기

T = int(input())

def same(arr):
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            break
    else:
        return arr

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            arr[i] = ''
            arr[i-1] = ''
    return same(list(''.join(arr)))


for x in range(T):
    li = list(input())

    print(f'#{x+1} {len(same(li))}')