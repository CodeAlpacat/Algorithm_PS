N, M = map(int, input().split())

N_set = set()
M_set = set()
for i in range(N):
    N_set.add(input())

for i in range(M):
    M_set.add(input())

a = sorted(list(N_set.intersection(M_set)))
print(len(a))
for i in a:
    print(i)