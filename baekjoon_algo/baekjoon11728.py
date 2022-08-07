N, M = map(int, input().split())
A = list(map(int, input().split()))
A.extend(list(map(int, input().split())))

print(*sorted(A))