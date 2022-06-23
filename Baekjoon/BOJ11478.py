# 서로 다른 부분 문자열의 길이

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
