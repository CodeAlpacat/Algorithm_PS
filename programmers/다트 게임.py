def solution(dartResult):
    #다음 숫자 직전까지 연산
    #만약 *이나 #이 들어있었으면 해당 인덱스를 저장하는 인덱스 리스트에 저장 및 안에 들어있는 인덱스에 모두 적용해줌.
    #리스트에 현재 계산 값을 담는다.
    save_num_idx = 0
    list_cal = []
    for i in range(len(dartResult)):

        if dartResult[i].isdigit() and i:
            if len(dartResult[save_num_idx:i]) != 1:
                if dartResult[save_num_idx-1] == '1':
                    list_cal.append('1' + dartResult[save_num_idx:i])
                else:
                    list_cal.append(dartResult[save_num_idx:i]) #연산 단위로 나눔
            
        if dartResult[i].isdigit():
            save_num_idx = i
    if dartResult[save_num_idx-1] == '1':
        list_cal.append('1' + dartResult[save_num_idx:len(dartResult)]) #마지막 연산
    else:
        list_cal.append(dartResult[save_num_idx:len(dartResult)]) #마지막 연산
    ans_mat = []
    for i in range(len(list_cal)):
        cur_num = 0
        if list_cal[i][0:2] == '10':
            cur_num = int(list_cal[i][0:2])
            if list_cal[i][2] == 'S':
                cur_num **= 1
            elif list_cal[i][2] == 'D':
                cur_num **= 2
            elif list_cal[i][2] == 'T':
                cur_num **= 3

            if list_cal[i][-1] == '*':
                if i != 0:
                    ans_mat[i-1] *= 2
                cur_num *= 2
            elif list_cal[i][-1] == '#':
                cur_num *= -1
            ans_mat.append(cur_num)
                
        else:
            cur_num = int(list_cal[i][0])
            if list_cal[i][1] == 'S':
                cur_num **= 1
            elif list_cal[i][1] == 'D':
                cur_num **= 2
            elif list_cal[i][1] == 'T':
                cur_num **= 3

            if list_cal[i][-1] == '*':
                if i != 0:
                    ans_mat[i-1] *= 2
                cur_num *= 2
                    
            elif list_cal[i][-1] == '#':
                cur_num *= -1
            ans_mat.append(cur_num)
        

    
    return sum(ans_mat)