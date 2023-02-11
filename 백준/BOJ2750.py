# 수 정렬하기

lst = [] # 숫자들을 담을 리스트

for _ in range(int(input())): # 첫 줄에 나오는 숫자만큼 반복
    num = int(input()) # 두번째 줄부터 리스트에 저장
    lst.append(num)

for i in sorted(lst): # 숫자를 정렬 후 출력
    print(i)