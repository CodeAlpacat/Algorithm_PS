#5185_이진수

T = int(input())
dict_hex = {
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}

for tc in range(T):
    N, hexa_num  = input().split()
    N = int(N)
    binary_num = ''
    for i in range(N):
        if hexa_num[i].isdigit():
            a = bin(int(hexa_num[i]))
            b = a[2:]
            while len(b) < 4:
                b = '0' + b
            binary_num += b
        else:
            binary_num += bin(dict_hex[hexa_num[i]])[2:]
    print(f'#{tc+1}', end = ' ')
    for i in binary_num:
        if i.isdigit():
            print(i, end ='')
    print()