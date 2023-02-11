# 명령 프롬프트

N = int(input()) # 파일 이름의 개수
filename = []

for _ in range(N): # 파일 이름을 filename 리스트에 저장
    a = input()
    filename.append(a)

result = list(filename[0]) # 리스트로 filename의 첫번째 값 저장

for i in range(N):
    for j in range(len(result)):
        if result[j] == filename[i][j]: # result와 filename 인덱스별로 비교 후 다르면 ?로 변환
            continue
        else:
            result[j]='?'

print(''.join(result))