# 오타맨 고창영
import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    tc = input().rstrip().split() # tc[0] = 지울 문자열 인덱스, tc[1] = 문자열
    tc[1] = tc[1][:int(tc[0])-1] + tc[1][int(tc[0]):] # tc[0]을 기준으로 앞뒤로 짜른 문자열을 더한다.
    print(tc[1])