N, M = map(int, input().split())

par = [i for i in range(N+1)]
rnk = [0 for _ in range(N+1)]

def find_(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_(par[x])
        return par[x]

def union_(a, b):
    a = find_(a)
    b = find_(b)

    if a == b:
        return

    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        rnk[a] += 1
        par[b] = a

mat = []
for i in range(M):
    mat.append(list(map(int, input().split())))

mat.sort(key = lambda x: x[2], reverse = True)
a, b = map(int, input().split())

for i in range(M):

    union_(mat[i][0], mat[i][1])
    if find_(a) == find_(b):
        print(mat[i][2])
        break