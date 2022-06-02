n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    #2의 n-j-1 제곱부터 시작 => 만약 i 번 인덱스 >= 2의 n-j-1 이면 빼주고 answer에 # 대입
    for i in range(len(arr1)):
        cur_arr1 = arr1[i]
        cur_arr2 = arr2[i]
        res_save = ''
        for j in range(n):
            flag1 = False
            flag2 = False
            if (2 ** (n-j-1)) <= cur_arr1:
                cur_arr1 -= (2 ** (n-j-1))
                flag1 = True
            

            if (2 ** (n-j-1)) <= cur_arr2:
                cur_arr2 -= (2 ** (n-j-1))
                flag2 = True
            
            if flag1 or flag2:
                res_save += '#'
            else:
                res_save += ' '
        answer.append(res_save)
            
        
    return answer