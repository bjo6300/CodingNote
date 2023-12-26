def solution(k, score):
    answer = []
    honor = [] # 명예의 전당
    
    for i in range(len(score)):
        honor.append(score[i]) 
        honor.sort(reverse = True) # 내림차순 정렬
        honor = honor[:k] # k만큼 짜르기
        answer.append(honor[-1]) # 명예의 전당 최하위 점수 추가
        
    return answer