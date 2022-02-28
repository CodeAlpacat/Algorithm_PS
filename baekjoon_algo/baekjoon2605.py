N = int(input())
li = [i for i in range(1, N+1)]
change = list(map(int, input().split()))

for i in range(len(change)):
    for j in range(i, i - change[i], -1):
        li[j], li[j-1] = li[j-1], li[j]

print(*li)