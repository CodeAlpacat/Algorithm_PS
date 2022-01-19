def my_avg(*args):
    sum = 0
    length_avg = 0
    for val in args:
        sum += val
        length_avg += 1
    avg = sum/length_avg
    return avg

print(my_avg(77, 83, 95, 80, 70))