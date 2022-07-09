# 첫 글자를 대문자로

N = int(input())

for _ in range(N):
    sentense = input()
    sentense = sentense[0].upper() + sentense[1:] # upper 함수로 문자열을 대문자로 만든다.
    print(sentense)