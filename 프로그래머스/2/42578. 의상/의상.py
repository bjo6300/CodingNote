def solution(clothes):
    dic = {}
    answer = 1
    
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]].append(clothes[i][0])
            
        else:
            dic[clothes[i][1]] = []
            dic[clothes[i][1]].append(clothes[i][0])
            
    
    for j in dic:
        answer *= len(dic[j]) + 1
        
    return answer - 1
    