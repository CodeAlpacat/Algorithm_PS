
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) #학교 수, 도로의 수
gender_info = [0] + list(input().split())

mat = [list(map(int, input().split())) for _ in range(M)]
mat.sort(key=lambda x: x[2])

par = [i for i in range(N+1)]
rnk = [0] * (N+1)

def find(x):
    if par[x] == x:
        return x

    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b):  
    
    a = find(a)
    b = find(b)
    
    if a == b:
        return

    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[b] < rnk[a]:
        par[b] = a
    else:
        par[a] = b
        rnk[b] += 1

print(*gender_info)

ans = 0
idx = 0
for i in range(M):
    a, b = mat[i][0], mat[i][1]
    
    if find(a) == find(b):
        continue
    
    if gender_info[a] != gender_info[b]:
        union(a, b)
        ans += mat[i][2]
        idx += 1

if idx == N-1:
    print(ans)
else:
    print(-1)