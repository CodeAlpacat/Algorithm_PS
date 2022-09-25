def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            s[i] = (ord(s[i]) + n)
            if s[i]>ord('z'):
                s[i] = s[i] - (ord('z')-ord('a')) - 1
            s[i] = chr(s[i])
        elif 'A' <= s[i] <= 'Z':
            s[i] = (ord(s[i]) + n)
            if s[i] > ord('Z'):
                s[i] = s[i] - (ord('Z')-ord('A')) - 1
            s[i] = chr(s[i])
            
    answer = ''.join(s)
    return answer