#스위치 켜고 끄기
#남학생은 받은 번호의 배수의 스위치 상태를 변경
#여학생은 좌우대칭, 가장 많은 수를 포함하는 구간의 스위치 변경
#구간의 스위치 = 홀수
switch_num = int(input())
switch = list(map(int, input().split()))
student_num = int(input())
for _ in range(student_num):
    student_gender, switch_num_student = map(int, input().split())
    if student_gender == 1:
        #남학생일 때,
        for i in range(len(switch)):
            if (i+1) % switch_num_student == 0: #배수이면 상태 바꿈
                if switch[i] == 0:
                    switch[i] = 1
                else:
                    switch[i] = 0
            else:
                continue
        
    
    elif student_gender == 2:
        #여학생일 때,
        if switch[switch_num_student-1] == 0:
            switch[switch_num_student-1] = 1
        else:
            switch[switch_num_student-1] = 0
        if switch_num_student in range(2, len(switch)-1): #맨 끝과 시작을 제외해야 홀수 개.
            for i in range(len(switch)//2+1):          
                if switch[switch_num_student-i-2] == switch[switch_num_student+i]: #양 옆의 수
                    
                    if switch[switch_num_student-i-2] == 0:
                        switch[switch_num_student-i-2] = 1
                        switch[switch_num_student+i] = 1
                    else:
                        switch[switch_num_student-i-2] = 0
                        switch[switch_num_student+i] = 0
                    
                    if switch_num_student-i-2 <=0 or switch[switch_num_student+i] >= len(switch)-1:
                        break

        elif 1 == switch_num_student:
            #시작
            if switch[0] == 0:
                switch[0] = 1
            else:
                switch[0] = 0
        elif len(switch) == switch_num_student:
            #끝
            if switch[len(switch)-1] == 0:
                switch[len(switch)-1] = 1
            else:
                switch[len(switch)-1] = 0

for i in range(len(switch)):
    print(switch[i], end = ' ')
# 아래와 무엇이 다를지 생각해보자.

# def change(num):
#     if switch[num] == 0:
#         switch[num] = 1
#     else:
#         switch[num] = 0
#     return


# N = int(input())
# switch = [-1] + list(map(int, input().split()))
# students = int(input())
# for _ in range(students):
#     gender, num = map(int, input().split())
#     # 남자
#     if gender == 1:
#         for i in range(num, N+1, num):
#             change(i)
#     # 여자
#     else:
#         change(num)
#         k = 1
#         while True:
#             if num + k > N or num - k < 1 : break
#             if switch[num + k] == switch[num - k]:
#                 change(num + k)
#                 change(num - k)
#             else:
#                 break
#             k += 1
                
# for i in range(1, N+1):
#     print(switch[i], end = " ")
#     if i % 20 == 0 :
#         print()