for ts in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    height_check = [0] * 101

    H = box[0]
    L = box[0]

    # 최고 높이, 최저 높이 설정 및 높이별 갯수 저장

    for height in box:
        height_check[height] += 1
        if H < height:
            H = height
        if L > height:
            L = height

    while dump > 0:
        if L >= H:
            break
        height_check[L] -= 1
        height_check[H] -= 1
        height_check[L + 1] += 1
        height_check[H - 1] += 1
        if height_check[L] == 0:
            L += 1
        if height_check[H] == 0:
            H -= 1

        dump -= 1

    print("#{} {}".format(ts + 1, H - L))