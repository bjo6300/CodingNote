# 홀수
lst=[]
flag = 0

for _ in range(7):
    num = int(input())
    if num % 2 != 0: # 홀수만 추출해서 리스트에 담는다.
        lst.append(num)
        flag = 1

if flag == 1:
    print(sum(lst))
    print(min(lst)) 
elif flag == 0: # 홀수가 없는 경우
    print(-1)