a,b = map(str, input().split())

answer = []

# +1 안하면 같을때 동작 안한다. -> a>=b
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    answer.append(cnt)

print(min(answer))

# A의 앞에 아무 알파벳이나 추가한다.
# A의 뒤에 아무 알파벳이나 추가한다.
# 위의 두 문장 어떻게 할지 고민하다가 모르겠어서 검색해봤는데 상관없는 문장이었다.. 브루트포스 문제

# a = abcd

# b = abcdef 이라고 가정했을때

# abcd

# (abcd)ef   ->   count = 0

# a(bcde)f   ->   count = 4

# ab(cdef)   ->   count = 4

# answer = [0, 4, 4]
# min(answer) = 0 이런식으로 동작할 것이다.