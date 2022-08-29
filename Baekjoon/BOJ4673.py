# 셀프 넘버

def d(n): # 생성자를 이용해 d(n) 구하기
    result = n
    for i in str(n):
        result += int(i)
    return result

non_self_num = set() # 셀프넘버가 아닌 수

for i in range(1,10001):
    non_self_num.add(d(i)) # d(n)을 이용해 셀프넘버가 아닌 수를 구한다.

for i in range(1, 10001):
    if i not in non_self_num: # 셀프넘버 출력
        print(i)
