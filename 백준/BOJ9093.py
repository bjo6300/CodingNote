# 단어 뒤집기

import sys
input = sys.stdin.readline

T = int(input().rstrip()) # 테스트 케이스 개수

for i in range(T):
    tc = input().split() # 테스트 케이스 리스트로 분리
    for j in tc:
        print(j[::-1], end=" ") # j[::-1]은 각 단어 뒤집은것, end=" "은 뒤집은 단어를 띄어쓰기로 이어붙인것
    print() # 이거 안하면 T줄짜리 문장이 한 문장으로 연결된다.