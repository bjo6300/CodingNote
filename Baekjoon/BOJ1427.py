input1 = input()

lst = []

# 리스트에 값을 저장
for i in input1:
    lst.append(i)

# reverse = True  내림차순
lst.sort(reverse=True)

# 리스트 출력
for i in lst:
    print(i, end='')