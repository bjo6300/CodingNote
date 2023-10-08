def solution(name, yearning, photo):
    answer = []
    
    for i in photo:
        result = 0
    
        for j in i: # j = 사진에 찍힌 인물
            if j in name: # name = 그리워하는 사람
                idx = name.index(j)
                result += yearning[idx]
                
        answer.append(result)
    
    return answer