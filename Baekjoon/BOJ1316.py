# 그룹 단어 체커

N = int(input()) # 단어의 개수
result = N

for i in range(N):
    word=input()
    for j in range(len(word)-1): # 인덱스를 j+1까지 이용하므로 -1
        if word[j] == word[j+1]: # 문자가 연속해서 나오는 경우
            pass
        elif word[j] in word[j+1:]: # -1하는 장본인 // 문자가 현재 인덱스+1부터 끝 안에 문자가 존재하면 result에서 -1
            result -= 1
            break
print(result)
