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

# #분해합
# #1~9 -> 자기스스로
# #10 -> 11 -> 13 이렇게 i의 분해합을 쭉 지나 N이 될때까지 찾는다.

# N = int(input())

# def div(n):

#     v = n
#     while n > 0:
#        v +=  n % 10
#        n //= 10 
#     return v


# for i in range(1, N+1):
#     if div(i) == N:
#         print(i)
#         break
#     if i == N:
#         print(0)

    


    

