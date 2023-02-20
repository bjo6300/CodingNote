def solution(n, words):
    check = []
    answer = []
    before_word = words[0]
    check.append(before_word)
    
    for i in range(1, len(words)):
        # 전 단어랑 이어지는지, 같은 단어를 말했는지
        if words[i][0] != before_word[-1] or words[i] in check:
            answer.append((i % n) + 1)
            answer.append(i // n + 1)
            break
        else:
            before_word = words[i]
            check.append(before_word)
    
    if len(answer) == 0:
        return [0, 0]
    else:
        return answer
    
    
        
    