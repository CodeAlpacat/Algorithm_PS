#슈퍼 마리오
#10개 버섯 일렬로
#슈퍼마리오는 순서대로 집으려함 중간에 중단가능. 먹는 것 중단 = 그 이후 못먹.
#점수의 합 100에 가깝게
mushroom_list = []
for i in range(10):
    mushroom_list.append(int(input()))

sum_result = 0
bigger_result = 0
for i in range(len(mushroom_list)):
    if sum_result + mushroom_list[i] <= 100:
        sum_result += mushroom_list[i] #100 전까진 계속 더해줌.
    else:
        bigger_result = sum_result + mushroom_list[i] # 한번만 더해주고 break
        break

if 100 - sum_result < bigger_result - 100:
    print(sum_result)
elif 100 - sum_result > bigger_result - 100:
    print(bigger_result)
elif 100 - sum_result == bigger_result - 100:
    print(bigger_result)