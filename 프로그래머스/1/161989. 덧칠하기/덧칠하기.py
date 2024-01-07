def solution(n, m, section):
    answer = 0
    section_num = section[0] + m
    for i in section:
        if section_num == i:
            answer += 1
            section_num = i + m
        elif section_num > i:
            continue
        elif section_num < i:
            answer += 1
            section_num = i + m
            
    return answer + 1