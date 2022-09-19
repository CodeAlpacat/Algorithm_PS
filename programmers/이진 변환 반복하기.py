def solution(s):
    answer = []
    cnt = 0
    total_zero = 0
    while int(s) > 1:
        save = len(s)
        a = len(s.replace('0', ''))
        total_zero += save - a
        s = bin(a)[2:]
        cnt += 1
    return [cnt, total_zero]