# 접미사 배열
S = input()

result = []

for i in range(len(S)):
    result.append(S[i:]) # 앞에 글자 떼고 하나씩 저장

result.sort() # 사전순으로 정렬

for i in result:
    print(i)