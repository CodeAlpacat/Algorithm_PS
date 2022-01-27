#분해합
#분해합 => N과 N을 이루는 각 자릿수의 합. 256 = 245 + 2 + 4 + 5
#N의 가장 작은 생성자를 구하는 코드. 256 -> 245
#그냥 1부터 모두 차례대로 넣어서 N이 나오면 break

N = int(input())

#x를 문자 단위로 슬라이싱해 다시 int로 바꿔 각 자릿수 더해줌.
def num_division(x):
    for i in str(x):
        x += int(i)
    return x

for i in range(1, N+1):
    if num_division(i) == N:
        print(i)
        break
    #생성자가 없는 경우는 생성자가 N을 탐색못하고 지나쳤을 때,
    if i == N:
        print(0)
    


    

