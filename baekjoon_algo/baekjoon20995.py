import sys
input = sys.stdin.readline

N, M = map(int, input().split())

par = [i for i in range(N+1)]
rnk = [0 for _ in range(N+1)]

def find_(a):
    if par[a] == a:
        return a
    else:
        par[a] = find_(par[a])
        return par[a]

def union_(a, b):
    a = find_(a)
    b = find_(b)

    if a == b:
        return
    
    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[b] < rnk[a]:
        par[b] = a
    else:
        rnk[a] += 1
        par[b] = a

    

cnt = 0
for i in range(1, M+1):
    node_a, node_b = map(int, input().split())
    #시냅스가 사이클을 이루면 안된다.
    if find_(node_a) != find_(node_b):
        union_(node_a, node_b)
    else:
        cnt += 1

neurons = set()
for i in range(1, N+1):
    neurons.add(find_(par[i]))

print(len(neurons) - 1 + cnt)