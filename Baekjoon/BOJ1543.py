# 문서 검색

document = input() # 문서
word = input() # 단어

count = 0

while True:
    if document.find(word) != -1 : # 찾았을 때
        count+=1
        document=document[document.find(word)+len(word):] # word의 인덱스 + word의 길이만큼 제거
    else: # 못 찾았을 때
        break

print(count)