# 팰린드롬 만들기
import sys
input = sys.stdin.readline

S = input().rstrip()

result = ''

for i in range(len(S)):
    result = S[i:] # S를 i부터 끝까지 복사
    if len(result) == 1 or result == result[::-1]: # result의 길이가 1인 case : abab, result == result[::-1]은 result가 펠린드롬
        print(len(S)+i) # S의 길이 + 추가한 문자의 길이
        break
