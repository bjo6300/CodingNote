# 파일 정리
import sys
input = sys.stdin.readline

N = int(input().rstrip())

file = {}

for _ in range(N):
    filename = input().rstrip().split('.') # 확장자만 뽑아내려면 .으로 분리
    
    if filename[1] in file: # 딕셔너리(file)에 저장
        file[filename[1]] += 1
    else:
        file[filename[1]] = 1

file = sorted(file.items(), key=lambda x:x[0], reverse=False) # sorted하면 딕셔너리 -> 리스트로 형변환된다.

for i in file:
    print(i[0], i[1])


"""
다른사람 코드

import sys
input = sys.stdin.readline

n = int(input())

file = dict()
for _ in range(n):
    extend = (input().split('.'))[1]
    if not extend in file:
        file[extend] = 1
    else:
        file[extend] += 1

sort_file = sorted(file.items())

for key, value in sort_file: 
    print(key.rstrip(), value)
"""