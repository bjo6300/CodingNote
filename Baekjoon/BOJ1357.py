# 뒤집힌 덧셈

X, Y = map(list, input().split())

result = []

# 문자열 또는 리스트로 받아야 [::-1] 가능

X = X[::-1] # Rev(X)
Y = Y[::-1] # Rev(Y)

X = ''.join(X) # 한 문자로 합치기
Y = ''.join(Y) # 한 문자로 합치기

# 정수로 변환 후 두 수를 더한다.
X = int(X) 
Y = int(Y) 
result.append(X+Y) 

result = list(map(str, result)) # int -> str
result = list(result[0])
result = ''.join(result[::-1]) # Rev(Rev(X)+Rev(Y))
result = int(result) # 이걸 안하면 5 5 넣었을 때 01이 나옴 // 중요
print(result)