N = int(input())
for i in range(N):
    num = int(input())
    if num >= 1900:
        print(f'Division {1}')
    elif 1600 <= num <= 1899:
        print(f'Division {2}')
    elif 1400 <= num <= 1599:
        print(f'Division {3}')
    else:
        print(f'Division {4}')



###############################

T = int(input())

for i in range(T):
    N = int(input())
    mat = list(map(int, input().split()))
    count_arr = [0] * 10010
    ans = -0xffffff
    for j in mat:
        count_arr[j] += 1

        if count_arr[j] >= 3:
            ans = max(ans, j)
    
    if ans < 0:
        print(-1)
    else:
        print(ans)


##################################


T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    even = False
    if arr[0] % 2 == 0:
        even = True 
    else:
        even = False 

    odd = False
    if arr[1] % 2 == 0:
        odd = True
    else:
        odd = False 

    ans = 'YES'
    for j in range(len(arr)):
        if j % 2 == 0:
            if arr[j] % 2 == 0:
                if even == False:
                    ans = 'NO'
                    break
            else:
                if even == True:
                    ans = 'NO'

        elif j % 2 == 1:
            if arr[j] % 2 == 1:
                if odd == True:
                    ans = 'NO'
                    break
            else:
                if odd == False:
                    ans = 'NO'
                    break
    print(ans)



###################################

# WWWWW
# 01234
# BRBBW flag를 찍자. 만약 이번에 R을 찍으면 1로 바꿈. 만약 flag == 1이면 다음은 무조건 B이고 바로 0으로 바꿈
# 0123 까지 RB or BR 시작 백트래킹
# 12110 B = 1 R = 2 W = 3
# 

T = int(input())

def recur(cur):
    global ans

    if original_mat[cur] != 'W':
        return

    if ans == 'YES':
        return
    

    if cur == N-1:
        for i in range(len(mat)):
            if mat[i] != original_mat[i]:
                return
            print(*original_mat)
        else:
            ans = 'YES'
        return
    
    original_mat[cur] = 'R'
    original_mat[cur+1] = 'B'
    recur(cur + 1)
    original_mat[cur+1] = 'W'
    original_mat[cur] = 'W'
    
    original_mat[cur] = 'B'
    original_mat[cur+1] = 'R'
    recur(cur + 1)
    original_mat[cur+1] = 'W'
    original_mat[cur] = 'W'

    recur(cur + 1)

for i in range(T):
    N = int(input())
    mat = list(input())
    original_mat = ['W'] * len(mat)
    ans = 'NO'
    recur(0)
    print(ans)


########################


T = int(input())

def recur(cur, flag):
    global ans
    if ans == 'YES':
        return
    

    if cur == N-1:
        for i in range(len(mat)):
            if mat[i] != original_mat[i]:
                return
            print(*original_mat)
        else:
            ans = 'YES'
        return
    if flag:
        recur(cur + 1, False)
    else:    
        original_mat[cur] = 'R'
        original_mat[cur+1] = 'B'
        recur(cur + 1, True)
        original_mat[cur+1] = 'W'
        original_mat[cur] = 'W'
        
        original_mat[cur] = 'B'
        original_mat[cur+1] = 'R'
        recur(cur + 1, True)
        original_mat[cur+1] = 'W'
        original_mat[cur] = 'W'

        recur(cur + 1, True)
for i in range(T):
    N = int(input())
    mat = list(input())
    original_mat = ['W'] * len(mat)
    ans = 'NO'
    recur(0, False)
    print(ans)