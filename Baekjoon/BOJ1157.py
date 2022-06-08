# 단어 공부

word = input()
word = word.upper() # 대문자로 받아오기

alpha_dict = {} # 알파벳과 빈도수를 저장할 딕셔너리

for i in word: # 딕셔너리 저장
    if i in alpha_dict:
        alpha_dict[i] += 1
    else:
        alpha_dict[i] = 1

alpha_dict = dict(sorted(alpha_dict.items(), key=lambda x :x[1], reverse=True)) # x[0]이 알파벳,x[1]이 빈도수이므로 빈도수를 내림차순으로 정렬
# dict로 형변환 한건 sorted하면 리스트로 반환되기 때문이다.

alpha_dict_keys = list(alpha_dict.keys()) # 알파벳만 분류
alpha_dict_values = list(alpha_dict.values()) # 빈도수만 분류

if len(alpha_dict_values) == 1: # 입력이 하나만 들어올 경우 두번째 elif에서 인덱스 오류가 뜨므로 예외처리
    print(alpha_dict_keys[0])
elif alpha_dict_values[0] == alpha_dict_values[1]: # max 알파벳이 여러개인 경우
    print('?')
else:
    print(alpha_dict_keys[0])