import copy
def solution(str1, str2):
    # 자카드 유사도 : 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
    answer = 0
    set_str1 = []
    set_str2 = []
    # 다중집합 원소로 만들기
    # 2글자씩, 영어 아니면 버리기, 대소문자 상관없음
    for i in range(len(str1) - 1):
        temp = str1[i : i + 2]
        
        if temp.isalpha():
            temp = temp.upper()
            set_str1.append(temp)
            
    for i in range(len(str2) - 1):
        temp = str2[i : i + 2]
        
        if temp.isalpha():
            temp = temp.upper()
            set_str2.append(temp)
    
    # ---

    temp_str1 = copy.deepcopy(set_str1)
    interaction_set = []
    union_set = copy.deepcopy(set_str1)

    if len(set_str1) == 0 and len(set_str2) == 0:
        return 65536
    else:
    
        # 다중합집합
        for i in set_str2:
            if i not in temp_str1: # str1에 없으면
                union_set.append(i)
            else: # str1에 있으면
                temp_str1.remove(i) # 중복 요소 제거
        # 다중교집합
        for i in set_str2:
            if i in set_str1:
                set_str1.remove(i)
                interaction_set.append(i)
    
    answer = len(interaction_set) / len(union_set)
    
    # 자카드 유사도 구하고 65536 곱하고 정수만 출력
    return (int(answer * 65536))