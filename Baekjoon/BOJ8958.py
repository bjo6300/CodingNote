# OX퀴즈

n = int(input())
lst = []

for _ in range(n):
    lst.append(input())

cnt = 0
score = 0

for i in range(n):
    for j in lst[i]:
        if j == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
    score=0
    cnt = 0