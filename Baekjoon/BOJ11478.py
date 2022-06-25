# 서로 다른 부분 문자열의 개수

import sys
input = sys.stdin.readline

S = input().rstrip()
result = []

for i in range(len(S)):
    for j in range(len(S)):
        if S[i:len(S)-j] =='':
            continue
        else:
            result.append(S[i:len(S)-j])

print(len(set(result)))


# S[i:len(S)-j] -> 서로 다른 부분 문자열
# 중복된 값도 들어가므로 set으로 중복제거를 한다.