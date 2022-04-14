N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

root = postorder[-1]
root_idx = 0
for i in range(len(inorder)):
    if inorder[i] == root:
        root_idx = i
        break

visited_in = [False] * (N+1)
visited_post = [False] * (N+1)
def checklft(cur): #중위의 왼쪽자식 중에서 후위의 가장 뒤쪽 찾기
    if visited_in[cur]:
        return
    max_idx = -1000000000
    inorder_idx = 0
    while cur-1 >=0: #중위의 왼쪽 인자
        record = 0
        for i in range(len(postorder)):
            if postorder[i] == inorder[cur]:
                record = i
        if max_idx < record:
            max_idx = record
            inorder_idx = cur
        cur -= 1
    
    visited_post[max_idx] = True
    visited_in[inorder_idx] = True
    

def preorder(cur):
    print(inorder[cur]) #루트 출력
    
    preorder() #()안의 값은 왼쪽 자식 최상단 루트 인덱스
    preorder()

# preorder(root_idx)

checklft(root_idx)

#중위의 오른자식에서 