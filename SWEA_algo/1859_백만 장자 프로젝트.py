# T = int(input())

# for x in range(T):
#     N = int(input())
#     price = list(map(int, input().split()))
#     price_copy = sorted(price, reverse=True)
#     idx = 0 #가장 큰값
#     max_price = price_copy[0]
#     sum_stack = 0
#     cnt = 0
#     for i in range(len(price)):
#         if price[i] < price_copy[idx]:
#             cnt += 1
#             sum_stack -= price[i] # 소비함.
        
#         elif price[i] == price_copy[idx]:
#             sum_stack += price_copy[idx] * cnt
#             cnt = 0 #다팔았으니 재고 초기화
#             if idx < len(price_copy):
#                 idx += 1 #최대값 다음으로 큰 값으로 감소
            
#     print(f'#{x+1} {sum_stack}')

T = int(input())

for x in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    cnt = 0
    first_val = price[len(price)-1]
    for i in range(len(price)-1, -1, -1): #거꾸로
        if first_val > price[i]:
            cnt += first_val - price[i]
        else:
            first_val = price[i]

    print(f'#{x+1} {cnt}')