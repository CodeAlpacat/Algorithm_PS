
def solution(info, query):
    answer = [0] * len(query)
    for i in range(len(info)):
        info[i] = list(info[i].split())
    for i in range(len(query)):
        a = query[i].split()
        del_set = {'and'}
        a = [i for i in a if i not in del_set]
        #- 가 포함되면 뭐가 들어가도 노상관
        
        
        
        for k in range(len(info)):
            if int(info[k][-1]) < int(a[-1]):
                continue
            if info[k][0][0] != a[0][0] and a[0] != '-':
                continue
                
            for j in range(4):
                if info[k][j] != a[j] and a[j] != '-':
                    break
                    
            else: 
                if int(info[k][-1]) >= int(a[-1]):
                    answer[i] += 1