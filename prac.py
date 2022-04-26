from collections import deque
import sys
# sys.stdin=open('sample_input.txt')
# import collections
import heapq

def find(x): #루트 찾기
    if par[x] == x: #자기스스로를 가리키면 자신 반환
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if rnk[a] < rnk[b]:
        par[a] = b
    elif rnk[a] > rnk[b]:
        par[b] = a
    else:
        par[a] = b #부모는 b(노상관)
        rnk[b] += 1 #부모의 랭크 증가


V, E = map(int, input().split()) #정점, 간선
mat = [list(map(int, input().split())) for _ in range(E)]

par = [i for i in range(V+1)] #자기자신이 부모인 노드들
rnk = [0] * (V+1) # 루트의 깊이를 판별할 랭크

mat.sort(key=lambda x: x[2]) #가중치 순으로 정렬

ans = 0
for i in range(E):
    a, b = mat[i][0], mat[i][1]
    
    if find(a) == find(b):
        continue
    
    union(a, b)
    ans += mat[i][2]

print(ans)