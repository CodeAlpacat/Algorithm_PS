import sys
sys.stdin.readline = input

paper_num = int(input())
li = [[0] * 1001 for _ in range(1001)]
cnt = 1
min_x = 10000000
min_y = 10000000
max_width = -11111
max_height = -11111
for tc in range(paper_num):
    x, y, width, height = map(int, input().split())
    
    for i in range(x, x+width):
        for j in range(y, y+height):
            li[i][j] = cnt
    cnt += 1

    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_width = max(width, max_width)
    max_height = max(height, max_height)

li_paper = [0] * (paper_num+1)
for i in range(min_x, len(li)):
    for j in range(min_y, len(li)):
        li_paper[li[i][j]] += 1

for i in range(1, len(li_paper)):
    print(li_paper[i])