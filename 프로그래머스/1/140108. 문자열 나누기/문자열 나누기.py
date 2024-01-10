def solution(s):
    x = s[0]
    x_count = 0
    un_x_count = 0
    answer = 0
    
    for i in range(len(s)):
        if x_count == un_x_count: # count가 같아지는 시점에 x, un_x count를 0으로 초기화하고 s[i]를 count해야한다.
            x = s[i] # 문자열을 분리하고 분리한 문자열의 첫 글자가 x
            answer += 1
            x_count = 0
            un_x_count = 0
            
        if s[i] == x:
            x_count += 1
        elif s[i] != x:
            un_x_count += 1
        
    return answer