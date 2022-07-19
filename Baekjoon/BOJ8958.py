# OX퀴즈

n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

cnt = 0 # 연속된 O의 개수
score = 0 # 총 점수

for i in range(n):
    for j in lst[i]: # lst에 넣은걸 차례대로 계산
        if j == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)

    score=0 # 다음을 위해 초기화
    cnt = 0 # 다음을 위해 초기화