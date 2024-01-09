def solution(babbling):
    answer = 0
    pronunciation = ["aya", "ye", "woo", "ma"]
    
    for bab in babbling:
        for pron in pronunciation:
            if pron * 2 in bab: # 같은 발음 연속되면 불가능
                break

            if pron in bab:
                bab = bab.replace(pron, "*")

            if bab == "*" * len(bab):
                answer += 1
                break
        
    return answer