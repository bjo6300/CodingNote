# 유학 금지

word = input()

lst =[]

for i in word:
    if i in 'CAMBRIDGE': # 알파벳이 'CAMBRIDGE'일 경우 
        continue
    else:
        lst.append(i) # 알파벳이 'CAMBRIDGE'이 아닐 경우 리스트에 추가

print(''.join(lst)) # 리스트에 있는 알파벳을 합쳐서 출력