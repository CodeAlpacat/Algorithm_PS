#슈퍼 마리오
score = 0
mushroom_list = []
for _ in range(10):
    mushroom_list.append(int(input()))

for i in range(10):
    copy_score = score
    score += mushroom_list[i]
    if score >= 100:
        small_result = 100 - copy_score
        bigger_result = score - 100
        if bigger_result <= small_result:
            print(score)
            break
        else:
            print(copy_score)
            break
else:
    print(score)