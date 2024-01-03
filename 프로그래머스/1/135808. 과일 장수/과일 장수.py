def solution(k, m, score):
    answer = 0
    score.sort(reverse = True) # 가격 높은 순으로 정렬
    
    for i in range(len(score) // m): # 전체 사과의 개수 // 한 상자에 들어가는 사과의 수 -> 남는 사과 버림
        slice_score = score[i * m : i * m + m] # 0~m, m~m+m, 2m~2m+m ...
        answer += min(slice_score) * m # 가장 낮은 점수 * m
    
    return answer