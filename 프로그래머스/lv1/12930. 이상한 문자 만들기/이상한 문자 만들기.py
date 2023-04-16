def solution(s):
    s = list(s)
    answer = ""
    index = 0
    for i in s:
        if i == " ":
            answer += " "
            index = 0
        elif index % 2 == 0:
            answer += i.upper()
            index += 1
        else:
            answer += i.lower()
            index += 1

    return answer