while True:
    try:
        N = int(input())
    except:
        break

    cnt = 0
    ans = 1
    while True:
        
        cnt = cnt * 10 + 1
        cnt %= N
        if cnt == 0:
            print(ans)
            break
        ans += 1