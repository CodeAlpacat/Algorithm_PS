#곱하기 혹은 더하기
#각자릿수가 0~9로 이루어진 문자열 S입력
#각 숫자들 사이에 + 나 *를 넣어 가장 큰 수를 만들자.
#모든 연산은 왼쪽부터 순차적으로 이루어진다.

#풀이 ->극단적으로 0122313이면 1 * 2 보다는 1+2가 더 커지므로 result 값이 0, 1이 나오면 더하기
S = input()
result = 0 #결과를 저장할 result 변수
for i in S:
    if int(i) == 1 or int(i) == 0 or result == 0 or result == 1:
        result += int(i)
    else:
        result *= int(i)

print(result)