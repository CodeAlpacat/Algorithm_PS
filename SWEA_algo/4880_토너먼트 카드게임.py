#4880 토너먼트 카드게임

def RPS(left, right):
    L = deck[left-1]
    R = deck[right-1]
    
    if L == R:
        return left
    elif L == 1:
        if R == 3:
            return left
        elif R == 2:
            return right
    elif L == 2:
        if R == 1:
            return left
        elif R == 3:
            return right
    elif L == 3:
        if R == 1:
            return right
        elif R == 2:
            return left
    

def recur(l, h):
    if l == h:
        return h
    
    return RPS(recur(l, (l+h)//2), recur((l+h)//2+1, h))

T = int(input())
for t in range(T):
    N = int(input())
    deck = list(map(int, input().split()))
    print(f'#{t+1} {recur(1, N)}')