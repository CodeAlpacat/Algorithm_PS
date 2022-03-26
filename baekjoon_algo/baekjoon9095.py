T = int(input())
def recur(total):
    res = 0

    if total > N:
        return 0

    if total == N:
        return 1

    for i in range(1, 4):
        res += recur(total + i)
    
    return res
for i in range(T):
    N = int(input())
    
    print(recur(0))