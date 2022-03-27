N = int(input())
divisor = [i for i in range(2, N)]
idx = 0
while idx < len(divisor):
    u = divisor[idx]
    divisor = [i for i in divisor if i <= u or i % u != 0]
    idx += 1

print(divisor)