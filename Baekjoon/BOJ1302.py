# 베스트 셀러

N = int(input())

title = {}

for _ in range(N):
    a = input()
    if a in title: # 단어가 딕셔너리에 있으면 숫자만 +1
        title[a] += 1
    else: # 딕셔너리에 없으면 단어를 추가하고 1로 설정
        title[a] = 1

max_book = max(title.values()) # 가장 많이 팔린 책의 숫자

result=[] # 가장 많이 팔린 책들 저장

for best_title, num in title.items(): # 키, 값 뽑아낼 반복문
    if num == max_book: 
        result.append(best_title)
    
print(sorted(result)[0]) # 중복이 있을 시 사전순으로 정렬 후 제목 출력