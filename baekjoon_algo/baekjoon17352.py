import sys
input = sys.stdin.readline

N = int(input())

par = [i for i in range(N+1)]
rnk = [0 for i in range(N+1)]

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
        par[a] = par[b]
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        par[a] = b
        rnk[b] += 1

for i in range(N-2):
    a, b = map(int, input().split())
    union_(a, b)

for i in range(1, N+1):
    if find_(par[i]) != find_(par[i+1]):
        print(par[i], par[i+1])
        break