#종이붙이기
def paper(cur):
    if memo[cur//10]:
        return memo[cur//10]

    if cur == 10:
        return 1
    elif cur == 20:
        return 3
    else:
        memo[cur//10] = paper(cur-10) + (2* paper(cur-20))
        return memo[cur//10]

T = int(input())

for x in range(T):
    N = int(input())
    memo = [0] * ((N//10)+1)
    print(f'#{x+1} {paper(N)}')
