# 상수

a, b = map(str, input().split()) # 숫자를 뒤집기 위해 str

a = int(a[::-1]) # 숫자를 뒤집고 비교하기위해 int
b = int(b[::-1])

print(a) if a > b else print(b) # 큰 수 출력