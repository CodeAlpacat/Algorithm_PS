#이진수2
T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = ""
    i = 1
    while True:
        if i >= 13:
            print(f"#{tc} overflow")
            break
        N *= 2
        if N == 1:
            result += "1"
            print(f"#{tc} {result}")
            break
        elif N > 1:
            N -= 1
            result += "1"
        else:
            result += "0"
        i += 1