# 모음의 개수

word = input()
count = 0

for i in word:
    if i in 'aeiou':
        count+=1

print(count)
