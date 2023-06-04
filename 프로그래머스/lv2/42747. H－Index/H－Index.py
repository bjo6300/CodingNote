def solution(citations):
    n = len(citations) # 발표한 논문
    citations.sort()
    
    for i in range(n):
        if citations[i] >= n - i: # h번 이상 인용된 논문이 h편 이상
            return n - i
    
    return 0

    