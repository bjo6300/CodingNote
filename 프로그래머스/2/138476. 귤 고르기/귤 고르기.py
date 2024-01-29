def solution(k, tangerine):
    dic = {}
    answer = 0
    for i in range(len(tangerine)):
        if tangerine[i] in dic:
            dic[tangerine[i]] += 1
        else:
            dic[tangerine[i]] = 1
    
    sorted_dic = dict(sorted(dic.items(), key = lambda x:-x[1]))
    temp = 0
    
    for i in sorted_dic.values():
        answer += 1
        temp += i
        if temp >= k:
            break
            
    return answer