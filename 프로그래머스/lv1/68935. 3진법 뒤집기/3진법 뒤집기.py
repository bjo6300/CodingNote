def solution(n):
    answer = ''

    while n > 0:			
        n, remainder = divmod(n, 3)	# n을 3으로 나눈 몫과 나머지
        answer += str(remainder) # 나머지 추가
    
    # 현재 answer = 앞뒤 반전 3진법
    
    return int(answer, 3) # int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌