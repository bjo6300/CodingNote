def solution(s, n):
    s = list(s) # 리스트로 변환
    for i in range(len(s)):
        if s[i].isupper(): # 대문자인 경우
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')) # 차를 구하고 나머지 연산 후 다시 ord('A')를 더한다.
        elif s[i].islower(): # 소문자인 경우
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a')) # 차를 구하고 나머지 연산 후 다시 ord('a')를 더한다.
        # 공백인 경우는 그대로
    return "".join(s)

    