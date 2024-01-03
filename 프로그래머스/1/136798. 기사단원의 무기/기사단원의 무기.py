def get_divisor_count(n, limit , power):
    cnt = 0
    
    for i in range(1, int(n ** (1/2)) + 1): # 제곱근만큼 반복
        
        if n % i == 0:
            
            if i == n // i: # 제곱근일 경우 -> 약수 1개
                cnt += 1
            else:
                cnt += 2 # 제곱근이 아닌 경우 약수 2개 (i, n // i)
                
        if cnt > limit: # 약수의 개수가 limit보다 크면 
            return power # power 반환
        
    return cnt

    
def solution(number, limit, power):
    total = 1 # power 범위 : 1 ~ limit
    
    for i in range(2, number + 1): # limit 범위 : 2 ~ 100
        total += get_divisor_count(i, limit, power)

    return total
