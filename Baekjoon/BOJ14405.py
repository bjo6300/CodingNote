# 피카츄
S = input()

# replace를 통해 "pi", "ka", "chu" 발음을 띄어쓰기로 바꾼다.
S = S.replace("pi", " ")
S = S.replace("ka", " ")
S = S.replace("chu", " ")

# .strip()을 통해 띄어쓰기를 붙였을 때 길이가 0이면 피카츄가 발음할 수 있는 문자열인 것이다.
if len(S.strip()) == 0:
    print("YES")
else:
    print("NO")