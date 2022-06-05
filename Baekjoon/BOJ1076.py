color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

# 3개 입력받기
input1 = input()
input2 = input()
input3 = input()

# input1, input2는 str 형식으로 숫자 그대로 연결한다.
# 그 이후 10^input3을 해서 input1+input2에 곱한다.
print(int(str(color.index(input1))+str(color.index(input2)))*(10**color.index(input3)))
