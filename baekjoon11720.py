N = int(input())
X = input()

count = 0
if len(X) != N:
    print(f"숫자의 개수가 {N}개가 아닙니다.")

else:
    for i in range(N):
        count += int(X[i])


print(count)
