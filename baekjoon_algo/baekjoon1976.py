N = int(input())
M = int(input())

#각 부모요소를 찾는다. 만약 부모노드가 다르면 union 같다면 pass
par = [i for i in range(N)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b):
    a = find(a)
    b = find(b)
    #노드의 깊이가 더 깊은 쪽이 부모가 됨
    if a < b:
        par[b] = a
    else:
        par[a] = b


for i in range(N):
    mat = list(map(int, input().split()))
    for j in range(N):
        if mat[j] == 1:
            union(i, j)

par = [-100000] + par
itinerary = list(map(int, input().split()))
prev = par[itinerary[0]]
for i in range(1, M):
    if prev != par[itinerary[i]]:
        print('NO')
        break

else:
    print("YES")
