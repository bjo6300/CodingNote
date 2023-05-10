def solution(a, b, n):
    # 빈 병 a를 가져다주면 콜라 b 병을 준다.
    answer = 0
    
    while n >= a:
        plus = n // a * b# 추가로 받은 콜라
        mod = n % a
        n = plus + mod
        answer += plus
    
    return answer