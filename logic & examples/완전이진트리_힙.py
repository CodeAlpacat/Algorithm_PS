H = [0] * 100 #미리 공간을 만들어놓음.
hsize = 0 #스택의 top과 같은 역할
# 0 1  2  3  4 5  6  7
# 0 20 15 19 4 13 11 ?

#   20
#  15 19
#4 13 11 23(?)추가

def enque(item):
    global hsize
    #full check => hsize == 99 인 상황 고려
    hsize += 1 # 새로 추가하기 위함.
    H[hsize] = item
    
    c = hsize
    p = hsize//2
    while p: # p가 루트에 접근하면 0이 됨.
        if H[p] >= H[c]: # 자식이 부모보다 크다면..
            break
        
        H[p], H[c] = H[c], H[p]
        c = p #값이 p를 2로 나눈 자리로 갔으므로 자식이 부모역할을 함. c = p
        p = c // 2 #새로운 부모에 대한 자식 인덱스 설정.
        #   20
        #  15 23
        #4 13 11 19 자리 바꿈.
        
def deque(): #첫 루트노드를 제거!
    global hsize
    ret = H[1]
    H[1] = H[hsize] #끝에 값을 첫값으로 저장
    hsize -= 1
    
    p, c  = 1, 2 # c: 왼쪽 자식
    
    while c <= hsize:
        if c + 1 <= hsize and H[c] < H[c+1]: #오른쪽이 더크면 c가 오른쪽 가리킴.
            c += 1
        if H[p] >= H[c]: #교환이 필요없는 상황.
            break
        H[p], H[c] = H[c], H[p]
        p = c
        c = p * 2
        
    return ret


# """
# 최대 100개의 정수
# 최대힙
# """

def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last  # 새로 추가된 정점을 자식으로
    p = c//2  # 완전이진트리에서의 부모 정점 번호
    while p > 0 and tree[p] < tree[c]:  # 부모가 있고, 자식의 키값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def deq():
    global last
    tmp = tree[1]  # 루트의 key값
    tree[1] = tree[last]  # 마지막 정점의 키를 루트에 복사
    last -= 1  # 마지막 정점 삭제
    # 부모 > 자식 규칙 유지
    p = 1
    c = p * 2  # 왼쪽자식노드 번호
    while c <= last:  # 왼쪽자식이 있으면
        if c + 1 <= last and tree[c] < tree[c+1]:  # 오른쪽자식도 있고 더 크면
            c += 1  # 오른쪽 자식 선택
        if tree[p] < tree[c]:  # 자식의 키값이 더 크면 교환
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


# 포화이진트리의 정점번호
tree = [0] * 101
last = 0  # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
# print(tree[1])
enq(9)
# print(tree[1])

while last > 0:
    print(deq(), tree[1])
    
