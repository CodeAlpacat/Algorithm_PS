N, K = map(int, input().split())

mat = [True for _ in range(N+1)]
mat[0] = False
mat[1] = False
cnt = 0
ans = 0
flag = False
for i in range(2, N+1):
    # if not mat[i]:
    #     continue
    
    for j in range(i, N+1, i):  
        if mat[j]:
            mat[j] = False
            cnt += 1
            print(j, cnt)
        if cnt == K:
            ans = j
            flag = True
            break
    if flag:
        break

print(ans)