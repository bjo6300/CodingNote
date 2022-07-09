# 거울, 오! 거울

while True:
    word = input()

    if word == "***": # ***을 입력하면 멈춤
        break
    
    print(word[::-1]) # 거꾸로 출력