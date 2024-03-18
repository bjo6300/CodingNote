def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)):
        if discount[i] not in want: # 원하는 제품이 없는 경우
            continue
        
        flag = 1
        temp_number = number.copy()  # deepcopy 대신 얕은 복사 사용
        
        numbers_len = sum(number)
        
        for j in range(i, numbers_len + i): # want 길이만큼 반복
            if j >= len(discount):  # 인덱스 오류 방지
                flag = 0
                break
            
            if discount[j] in want:
                idx = want.index(discount[j])
                temp_number[idx] -= 1
                
                if temp_number[idx] < 0:
                    flag = 0
                    break
            else:
                flag = 0
                break
        
        if flag == 1:
            answer += 1
            
    return answer