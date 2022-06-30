#nCm = n부터시작해서 m개만큼..

N, M = map(int, input().split())
def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)

# 100까지라면 1~ 100까지는 5가 최소 하나씩 존재
# 5로 나누면 20개의 5를 구했음
# 한번 더 나누고 개수를 구하면 5가 2개 들어간 수를 구할 수 있음.