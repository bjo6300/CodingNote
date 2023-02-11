# # 3의 배수

# readline을 사용하기 위해 import합니다.
from sys import stdin

# 첫째 줄에 큰 자연수 X를 입력합니다.
# 1,000,000자리 이하의 수입니다.
# 입력한 X를 각 자리수의 숫자들을 정수형으로 변환하고 리스트 변수로 만들어줍니다.
X = list(map(int, list(stdin.readline().rstrip())))
# 문제 변환의 과정 횟수를 저장할 변수를 선언합니다.
phase = 0

# 한 자리수로 될 때가지 문제 변환을 반복합니다.
while True:
    # 변환된 X의 길이가 1이라면
    if len(X) == 1:
        # 문제 변환의 과정 횟수를 출력합니다.
        print(phase)
        # X가 3, 6, 9 중 하나라면
        if int(X[0]) in [3, 6, 9]:
            # YES를 출력하고 반복문을 탈출합니다.
            print("YES")
            break
        # X가 3, 6, 9 중 하나가 아니라면
        else:
            # NO를 출력하고 반복문을 탈출합니다.
            print("NO")
            break

    # X에 문젠 변환의 과정을 거칩니다.
    # 각 자리수의 숫자인 리스트 변수인 X의 합을 구하고
    # 그 결과의 각 자리수의 숫자를 또 리스트 변수로 만들어줍니다.
    X = list(map(int, list(str(sum(X)))))
    # 문제 변환의 과정 횟수에 1을 더해줍니다.
    phase += 1


# # 94%에서 틀림..
# X = input()

# count = 0

# result = 0

# while 1:
#     result = 0
#     for i in str(X):
#         result += int(i)
#     count+=1
#     X = result
#     if result < 10:
#         break

# print(count)
# if int(X) % 3 == 0:
#     print('YES')
# else:
#     print('NO')
