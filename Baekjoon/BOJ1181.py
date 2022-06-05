# 단어 정렬
N=int(input()) # 입력받을 개수
result=[] # 결과값 배열로 저장

for i in range(0,N): # 개수만큼 입력받고 result에 저장
    result.append(input())

result=list(set(result)) # set을 이용해 중복 제거
result.sort() # 알파벳 순으로 정렬
result.sort(key=len) # 길이 순으로 정렬

for i in result:
    print(i)