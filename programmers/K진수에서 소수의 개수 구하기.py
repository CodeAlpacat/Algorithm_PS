from collections import deque

def solution(n, k):
    def sosu(num):
        for i in range(2, num):
            if i * i > num:
                return True
            
            if not num % i:
                return False
            
        else:
            return True
    conv_str = ''
    if k <= 9:
        q = deque([])
        while n:
            n, m = divmod(n, k)
            q.appendleft(str(m))

        conv_str = ''.join(q)
    else:
        conv_str = str(n)
    
    
    
    mat = list(conv_str.split('0'))
    cnt = 0    
    for i in mat:
        if len(i) and int(i) != 1 and sosu(int(i)):
            cnt += 1
    
    return cnt