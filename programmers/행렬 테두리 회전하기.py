

def solution(rows, columns, queries):
    global mat
    mat = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = cnt
            cnt += 1
            
    def rotate(x1, y1, x2, y2):
        
        prev = mat[x1][y1-1]
        min_num = prev
        for i in range(y2-y1):
            mat[x1-1][y1-1+i], prev = prev, mat[x1-1][y1-1+i]
            min_num = min(min_num, prev)
            
        for i in range(x2-x1):
            mat[x1-1+i][y2-1], prev = prev, mat[x1-1+i][y2-1]
            min_num = min(min_num, prev)
            
        for i in range(y2-y1):
            mat[x2-1][y2-1-i], prev = prev, mat[x2-1][y2-1-i]
            min_num = min(min_num, prev)
        for i in range(x2-x1):
            mat[x2-1-i][y1-1], prev = prev, mat[x2-1-i][y1-1]
            min_num = min(min_num, prev)

        return min_num
    answer = []
    
    
    for i in queries:
        answer.append(rotate(i[0], i[1], i[2], i[3]))
    
    return answer