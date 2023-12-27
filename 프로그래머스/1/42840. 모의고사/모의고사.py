def solution(answers):
    num = [0, 0, 0]
    math_fail1 = [1, 2, 3, 4, 5]
    math_fail2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_fail3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == math_fail1[i % len(math_fail1)]:
            num[0] += 1
        if answers[i] == math_fail2[i % len(math_fail2)]:
            num[1] += 1
        if answers[i] == math_fail3[i % len(math_fail3)]:
            num[2] += 1
    
    answer = []
    
    for i in range(3):
        if num[i] == max(num):
            answer.append(i + 1)
            
    return answer