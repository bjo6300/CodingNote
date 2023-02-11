# 단어 나누기

word = list(input()) # 단어를 리스트로 받는다.
result = [] # 만들어진 모든 단어 저장
tmp = [] # 만들어진 모든 단어를 문자별로 저장한 리스트

for i in range(1, len(word) - 1): # 적어도 길이가 1이상 나눈다.
    for j in range(i + 1, len(word) ):
        a = word[:i] # 최소 [0:1], 최대 [0:5]
        b = word[i:j] # 최소 [1:2] 최대 [1:6]
        c = word[j:] # 최소 [2:len(word)] 최대 [6:len(word)]
        a.reverse() # 리스트만 reverse 가능
        b.reverse()
        c.reverse()
        tmp.append(a + b + c) # ex) ['m', 'o', 'l', 'e', 't', 'i', 'b']

for a in tmp: # ['m', 'o', 'l', 'e', 't', 'i', 'b'] -> moletib로 연결
    result.append(''.join(a))

print(sorted(result)[0]) # 사전순으로 정렬된것 중 첫번째것 출력