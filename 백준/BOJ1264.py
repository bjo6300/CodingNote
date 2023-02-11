# 모음의 개수

testcase = [] # 입력 테스트 케이스
count = 0 # 모음의 개수 
while True:
    a = input()
    if a == '#':
        break

    testcase.append(a) # 문장 입력받아서 리스트에 저장

for i in testcase:
    for j in i:
        if j in 'aeiouAEIOU': # 테스트 케이스의 문장에서 인덱스별로 aeiouAEIOU가 있는지 비교
            count +=1
    print(count)
    count = 0

# while 1:
#     s = input()
#     if s == '#':
#         break
#     cnt = 0

#     for c in s:
#         if c in 'aeiouAEIOU':
#             cnt += 1
#     print(cnt)
