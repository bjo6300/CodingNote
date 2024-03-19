def solution(s):
    answer = []
    s = s[2 : -2] # 앞뒤 {{, }} 제거
    s = s.split("},{") # },{ 기준으로 나누기
    s.sort(key = len) # 길이 순으로 정렬

    for i in s:
        i_list = i.split(',') # 튜플을 , 기준으로 나누기

        for j in i_list:
            if int(j) not in answer: # 중복되지 않는 숫자만 추가
                answer.append(int(j))
    return answer