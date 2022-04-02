N = int(input())
lft = {}
rgt = {}
for i in range(N):
    a, b, c = input().split()

    lft[a] = b
    rgt[a] = c


def dfs(cur, option):
    if cur == '.':
        return

    if option == 0:
        print(cur, end='')

    dfs(lft[cur], option)
    if option == 1:
        print(cur, end='')

    dfs(rgt[cur], option)
    if option == 2:
        print(cur, end='')

dfs('A', 0)
print()
dfs('A', 1)
print()
dfs('A', 2)