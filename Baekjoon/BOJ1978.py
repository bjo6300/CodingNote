# 소수 찾기

N = int(input())
num = list(map(int, input().split())) # input().split() 하려다가 입력받는 값이 문자열로 들어와서 map을 사용
result = 0

for i in num:
    for j in range(2, i+1):
        if i%j == 0: # 나누어 떨어지고
            if i == j: # 나누어 떨어진게 자기 자신이면 소수
                result+= 1
            break

print(result)
