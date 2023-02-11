# 백대열

n,m = map(int, input().split(':'))

def gcd(x,y): # 유클리드 호제법
    # 큰 수를 작은 수로 나눈 나머지를 구한다.
    # 나눴던 수와 나머지로 또 mod 연산을 한다.
    # 이 과정을 계속 반복해 0이 됐을 때 마지막 계산에서 나누는 수로 사용된 숫자가 최대공약수가 된다.
    while y>0:
        temp = x
        x = y
        y = temp % y
    return x

result = gcd(n,m) # 유클리드 호제법으로 구한 최대공약수

print('%d:%d' %(n//result, m//result))

# gcd를 사용하기 위해 import합니다.
from math import gcd

# n과 m을 :을 사이에 두고 입력합니다.
# 1 <= n, m <= 100,000,000
# 각각 정수형으로 변환합니다.
n, m = map(int, input().split(':'))
# n과 m의 최대공약수를 저장하는 변수를 선언합니다.
gcd_num = gcd(n, m)

# n과 m을 gcd_num으로 나눈 몫들을 출력 형식에 맞게 출력합니다.
print(f"{n // gcd_num}:{m // gcd_num}")