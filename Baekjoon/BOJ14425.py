# 문자열 집합

N, M = map(int, input().split()) 

S = []
count = 0

for _ in range(N):
    S.append(input()) # N개의 개수만큼 단어를 S에 저장

for _ in range(M):
    M_word = input()
    if M_word in S: # 입력받는게 S안에 있으면 count 증가
        count +=1

print(count)
