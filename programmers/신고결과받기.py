def solution(id_list, report, k):
    id_dict = {}
    for i in range(len(id_list)):
        id_dict[id_list[i]] = i
    
    report = list(set(report))
    reported_info = [[] for _ in range(len(id_list))]
    
    mat = [0] * len(id_list)
    
    #신고당한 횟수
    for i in range(len(report)):
        info0, info1 = report[i].split()
        mat[id_dict[info1]] += 1
        reported_info[id_dict[info0]].append(info1)
    
    banned_id = []
    for i in range(len(mat)):
        if mat[i] >= k:
            banned_id.append(id_list[i])
            
    answer = [0] * len(id_list)
    
    for i in range(len(reported_info)):
        for j in range(len(banned_id)):
            if banned_id[j] in reported_info[i]:
                answer[i] += 1
    return answer