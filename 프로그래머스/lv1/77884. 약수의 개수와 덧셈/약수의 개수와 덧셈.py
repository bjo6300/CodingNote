import math
def solution(left, right):
    result = 0
    for num in range(left, right + 1):
        if num == 1:
            answer = [1]
        else:
            answer = [1, num] # 1과 자기자신 추가
        
        for i in range(2, int(num ** 0.5) + 1): # 1과 자기자신을 제외한 약수들 구하기
            if num % i == 0: # 약수 구하기
                answer.append(i)
                if num // i != i: # 약수일 경우 거기에 맞는 짝 구하기
                    answer.append(num // i)
                    
        if len(answer) % 2 == 0:
            result += num
        else:
            result -= num
    
    return result