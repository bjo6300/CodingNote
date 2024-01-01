from itertools import combinations

def is_prime(n): # 소수 판별
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for combi in combinations(nums, 3): # 조합으로 
        plus = sum(combi)
        
        if is_prime(plus): # 합이 소수면 +1
            answer += 1

    return answer