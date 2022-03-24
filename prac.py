import sys
sys.stdin=open('sample_input (6).txt')
T = int(input())
secret_origin = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
bi_convert = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
    }
ratio_bi = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}


def check_secret():
    ans = 0
    for h in range(len(secret_table)):
        bi_change = ''
        for j in range(len(secret_table[h])):
            bi_change += bi_convert[secret_table[h][j]]
        bi_change = bi_change.rstrip("0")
        t = bi_change

        arr_ratio = []
        cnt1 = cnt2 = cnt3 = cnt4 = 0
        for i in range(len(t)-1, -1, -1):
            
            if t[i] == '1' and cnt2 == 0:
                cnt1 += 1
            elif t[i] == '0' and cnt3 == 0:
                cnt2 += 1
            elif t[i] == '1' and cnt4 == 0:
                cnt3 += 1
            elif t[i] == '0':
                if t[i-1] == '1':
                    cnt = min(cnt1, cnt2, cnt3)
                    arr_ratio.append(ratio_bi[cnt3//cnt, cnt2//cnt, cnt1//cnt])
                    cnt1 = cnt2 = cnt3 = 0
                    if len(arr_ratio) == 8:
                        a = arr_ratio[1] + arr_ratio[3] + arr_ratio[5] + arr_ratio[7]
                        b = arr_ratio[0] + arr_ratio[2] + arr_ratio[4] + arr_ratio[6]
                        if (a * 3 + b) % 10 == 0:
                            if arr_ratio not in visited:
                                visited.append(arr_ratio)
                                ans += (a+b)
                        arr_ratio = []
    return ans

for tc in range(T):
    N, M = map(int, input().split())
    secret_table = sorted(list(set([input()[:M] for _ in range(N)])))
    secret_table.pop(0)
    visited = []
    ans = check_secret()
    print(f'#{tc+1} {ans}')