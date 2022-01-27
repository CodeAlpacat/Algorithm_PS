#나는 요리사다
result = 0
count = 1
winner = 0
for i in range(5):
    score_list = list(map(int, input().split()))
    if result < sum(score_list):
        result = sum(score_list)
        winner = count
    count += 1

print(winner, result)
    