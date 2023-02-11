# 괄호

T = int(input())

for _ in range(T): # T개만큼 반복
    testcase = list(input()) # 괄호를 list로 받음
    sum = 0

    for i in testcase: 
        if i == "(": 
            sum +=1
        elif i == ")":
            sum -= 1
        if sum < 0: # )가 더 많은 경우  # 예시  ()) 같은 경우
            print("NO")
            break
    if sum == 0: # 0이면 VPS
        print("YES")
    elif sum > 0: # 양수면 (가 더 있는 경우
        print("NO")