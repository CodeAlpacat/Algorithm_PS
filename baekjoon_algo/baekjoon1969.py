
#TAAGATAC

#TATGATAC 1
#TAAGCTAC 1
#AAAGATCC 2
#TGAGATAC 1
#TAAGATGT 2

#A T G C

#[0, 0, 0, 0, 0] => A T G C 넣음. 세로로 가면서 해당하면 리스트 인덱스 증가

N, M = map(int, input().split())

mat = [input() for _ in range(N)]
dna_dict = {'A':0, 'T':0, 'G':0, 'C': 0}

ans = ''
cnt = 0
for i in range(M):
    for j in range(N):
        dna_dict[mat[j][i]] += 1

    max_value = -0xffffff
    cur_str = ''
    for idx, val in dna_dict.items():
        if dna_dict[idx] > max_value:
            max_value = dna_dict[idx]
            cur_str = idx
        elif dna_dict[idx] == max_value and ord(idx) < ord(cur_str):
            max_value = dna_dict[idx]
            cur_str = idx
    ans += cur_str

    for j in range(N):
        if cur_str != mat[j][i]:
            cnt += 1

    for j in range(N):
        dna_dict[mat[j][i]] = 0
            
print(ans)
print(cnt)