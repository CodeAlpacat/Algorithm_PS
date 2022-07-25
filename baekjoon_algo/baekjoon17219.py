N, M = map(int, input().split())

site_dict = {}

for i in range(N):
    site, pw = input().split()
    site_dict[site] = pw

find_list = []
for i in range(M):
    find_list.append(site_dict[input()])

for i in find_list:
    print(i)