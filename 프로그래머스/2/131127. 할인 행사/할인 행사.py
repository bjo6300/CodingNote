def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)):
        if discount[i] not in want: # 처음에 원하는 제품이 없는 경우
            continue
        
        flag = 1 # 모두 할인 받는 경우 : 1
        temp_number = number.copy()  
        
        for j in range(i, 10 + i):
            if j >= len(discount):  # 인덱스 오류 방지
                flag = 0
                break
            
            if discount[j] in want: # 범위 내에 원하는 제품이 있는 경우
                idx = want.index(discount[j])
                temp_number[idx] -= 1
                
                if temp_number[idx] < 0:
                    flag = 0
                    break
            else: # 범위 내에 원하는 제품이 없는 경우
                flag = 0
                break
        
        if flag == 1:
            answer += 1
            
    return answer