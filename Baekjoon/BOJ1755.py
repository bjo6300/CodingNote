# 숫자놀이

M, N = map(int, input().split())

eng_num = [[0,'zero'],[1,'one'],[2,'two'],[3,'three'],[4,'four'],[5,'five'],[6,'six'],[7,'seven'],[8,'eight'],[9,'nine']] # 숫자, 숫자에 맞는 영어단어 저장

result = []

for i in range(M,N+1): # M 이상 N 이하 범위
    eng_name = ''
    for j in str(i): # 10이면 1 따로 0 따로해서 영어 단어를 합쳐서 저장 'one zero' 이런식으로
        eng_name += ' ' + eng_num[int(j)][1]
        
    result.append([int(i),eng_name]) # 합친 단어를 [숫자, 영어단어] 형식으로 저장

result.sort(key=lambda x:x[1]) # 영어단어를 기준으로 오름차순 정렬

t = 0

for i in range(len(result)): # 10개씩 출력
    t += 1

    print(result[i][0], end=' ')

    if t == 10:
        print()
        t = 0    