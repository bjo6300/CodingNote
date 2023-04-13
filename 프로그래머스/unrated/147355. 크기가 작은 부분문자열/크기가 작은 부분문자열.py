def solution(t, p):
    sub_strings = []
    answer = 0
    
    for i in range(len(t) - len(p) + 1):
        sub_strings.append(t[i:i + len(p)])
    
    for s in sub_strings:
        if p >= s:
            answer += 1

    return answer