n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    cnt = 0
    for j in range(i+1):
        res = i+ cnt
        res %= 26
        res += 65
        print(chr(res), end=' ')
        cnt += n-j-1
    print()