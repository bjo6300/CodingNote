# 크로아티아 알파벳
word = input()

c_alpha = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 크로아티아 알파벳

for i in c_alpha:
    word = word.replace(i,'c') # 크로아티아 알파벳 을 문자 'c'로 바꿔 길이를 구한다.

# 크로아티아 알파벳은 분리되지 않으므로 한 글자로 세고, c_alpha에 없는 알파벳도 한 글자씩 세므로 크로아티아 알파벳을 한 글자의 알파벳으로 바꿔 구하면 된다.
print(len(word))