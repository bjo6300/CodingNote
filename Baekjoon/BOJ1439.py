# 뒤집기

# input1 = input()

# input_0 = 0 # 0의 개수
# count = 0
# result = ''
# for n in input1:
#     if n == '0': 
#       input_0+=1

# input_1 = len(input1) - input_0 # 1의 개수

# while True:
#     if input_0 > input_1: # 0이 더 많을 때 1을 0으로 변환
#         for r in input1:
#             if r == '1':
#                 result += str(r)
#                 count += 1
#         break
#     else: # 1이 더 많을 때 0을 1로 변환
#         for r in input1:
#             if r == '0':
                
#                 result += str(r)
#                 count+=1
#         break

# print(count)

## 0, 1의 개수가 적은 것을 뒤집는줄 알고 구현했다가 문제를 잘못 이해했단걸 깨달았다..

# 답지
s = input()

cnt = 0 
for i in range(len(s)-1): # for문에서  i와 i+1의 요소를 비교할 것이기 때문에 len(s)-1로 해줘야한다.
    if s[i] != s[i+1]:
        cnt += 1

print((cnt+1)//2)
    
