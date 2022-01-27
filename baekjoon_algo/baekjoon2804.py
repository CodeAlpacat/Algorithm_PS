#크로스워드 만들기
#두 단어를 입력받아 같은 문자를 공유하는 지점을 교차하도록 해야한다.
# A는 가로, B는 세로
#A의 첫 글자부터 겹친다면 B의 처음 겹치는 줄에 A를 겹칩니다.
A, B = input().split()

#일단 겹치는 인덱스부터 찾자!
#가로 5
cross_word_index_Ver = 0
for i in A:
    if B.find(i) != -1:
        cross_word_index_Ver = B.find(i)
        cross_word_index_Hor = A.find(i)
        break
    else:
        continue
# 세로 2


#이젠 반복만 남음

for i in range(len(B)): #BBBA hor = 1 
    for j in range(len(A)): #ABBB ver = 3
        if cross_word_index_Hor == j:
            print(B[i], end ='')
        else:
            if cross_word_index_Ver == i:
                if cross_word_index_Hor == 0:
                    print(A[1:], end ='')
                    break
                else:
                    print(A, end ='')
                    break
            else:
                print('.', end = '')
    print()