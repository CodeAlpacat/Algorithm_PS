# 2023. 신기한 소수 (1번템플릿 & 정수론)
# 0000
# 0001
# 0002
# 0003
# ...
# 9999

# 앞에서 가면서 소수가 아닌걸 짤라내면된다.

n = int(input())

# 정수론을 보고 바꿔주면된다.
def check(n):
    cnt = 0
    if n == 1:
        return False
    
    for i in range(1,n+1):
        if i*i > n:
            break
        
        if n%i ==0:
            cnt += 1
    return n == 0 or cnt == 2        

def recur(cur,num):
    # 두전째 생각 재귀 들어가고 처리 cur = 0 인 경우 예외처리
    # 가지치기
    if cur!= 0 not check(num):
        return 

    # 기저
    if cur == n:
        print(num)
        return
    
    # 재귀호출
    for i in range(1,10):
        # 첫번째 생각 . 선호하지는 않는다.
        #if check(10*num+i):
	    #    recur(cur+1,10*num+i)
        recur(cur+1,10*num+i)
recur(0,0)    	