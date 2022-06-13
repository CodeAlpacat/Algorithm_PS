def solution(cacheSize, cities):
    answer = 0
    #만약 안에 같은 문자열이 없다면, 하나씩 append하고 pop(0) 한 후, + 5
    #같은 문자열이 있다면, 해당 인덱스 pop() 후에, 리턴값 append하고 + 1
    cities = list(map(lambda x: x.lower(), cities))
    cache = []
    res = 0
    for i in range(len(cities)):
        if cache.count(cities[i]):
            for j in range(len(cache)):
                if cities[i] == cache[j]:
                    cache.append(cache.pop(j))
                    res += 1
                    break
        elif len(cache) == cacheSize:
            cache.append(cities[i])
            cache.pop(0)
            res += 5
        else:
            cache.append(cities[i])
            res += 5
        
    return res