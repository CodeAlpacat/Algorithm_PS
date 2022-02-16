def check(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True

    if arr[0] == arr[-1]:
        return check(arr[1:len(arr)-1])

T = int(input())

for x in range(T):
    N = list(input())
    
    if check(N):
        print(f'#{x+1} 1')
    
    else:
        print(f'#{x+1} 0')