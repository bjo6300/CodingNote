# 무한 문자열

s = input() 
t = input() 

if s * len(t) == t * len(s): # s에는 t의 길이, t에는 s의 길이를 곱해 s와 t의 길이를 같게 만들고 비교한다.
    print('1')
else:
    print('0')

'''
# 다른사람 코드
import sys
input = sys.stdin.readline
from math import gcd # 최대공약수

s = input().rstrip()
t = input().rstrip()
n = len(s)
m = len(t)
a = gcd(n,m) # 최대공약수
if s*(m//a) == t*(n//a): # 최대공약수를 이용해 최소공배수만큼 문자를 만들어 비교했다.
    print(1)
else:
    print(0)
'''