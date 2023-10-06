def solution(food):
    result = ''
    
    for i in range(1, len(food)): # food[0] = 물
        temp = food[i] // 2 # 두 선수가 먹을 양
        result += str(i) * temp # 음식 종류 * 두 선수가 먹을 양
    
    answer = result + "0" + result[::-1]
    
    return answer