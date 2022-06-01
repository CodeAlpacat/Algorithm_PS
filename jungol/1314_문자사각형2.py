n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            a = i + n*j
            a %= 26
            a += 65
            print(chr(a), end=' ')
        else:
            b = n*(j+1)-1 - i
            b %= 26
            b += 65
            print(chr(b), end=' ')
    print()

#65 72 73 80
#66 71 74 79
#67 70 75 78
#68 69 76 77

#0 7 8 15
#1 6 9 14
#2 5 10 13
#3 4 11 12