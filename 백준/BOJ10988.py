# 팰린드롬인지 확인하기


## 맞음
word = list(input())
if word == word[::-1]:
    print('1')
else:
    print('0')

## 틀림, 반례 -> abbc

# word = input()

# i = 0
# temp = 0
# for _ in range(len(word)//2):
#     if word[i] == word[-(i+1)]:
#         temp = 1
#     else:
#         temp = 0
#     i+=1
# print(temp)