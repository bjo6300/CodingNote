def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]: # 양수
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer