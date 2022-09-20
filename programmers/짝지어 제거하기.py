# def solution(s):
#     save = len(s)
#     a = list(map(ord, list(set(s))))
    
#     while len(s):
        
#         for i in range(len(a)):
#             s = s.replace(chr(a[i])*2, '')
        
#         if len(s) == save:
#                 return 0
#         else:
#             save = len(s)

#     return 1

def solution(s):
    stack = []
    cnt = 0
    for i in s:
        
        if not len(stack) or stack[-1] != i:
            stack.append(i)
        else:           
            stack.pop()
    
    if len(stack) > 0:
        return 0
        
    return 1