# 팰린드롬수

testcase = [] # 테스트케이스 저장

while 1:
    a = input()
    if a == '0': # 0이면 break
        break
    else: 
        testcase.append(a)

front = 0 # 문자의 처음 인덱스
last = 1 # 문자의 마지막 인덱스 (ex : word[-1])
temp = True # print문 판별

for num in testcase:
    for _ in range(len(num)//2): # num을 2로 나눈 몫만큼 실행
        if num[front] != num[-last]: # 처음 인덱스 문자와 마지막 인덱스 문자가 다르면 False -> no 출력
            temp = False
        
        front +=1 # 처음, 마지막 인덱스 증가
        last += 1

    front = 0 # 처음, 마지막 인덱스 초기화
    last = 1

    if temp == False:
        print('no')
    else:
        print('yes')

    temp = True # 판별 초기화

# while True:
#     input_num = input()
    
#     if input_num == "0":
#         break
    
#     answer = "no"


#     if input_num == input_num[::-1]:
#         answer = "yes"
    
#     print(answer)