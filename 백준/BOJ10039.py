# 평균 점수

result = 0

for _ in range(5):
    score = int(input())
    if score < 40:
        score = 40
    result += score

print(int(result/5))