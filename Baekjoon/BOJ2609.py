# 최대공약수와 최소공배수

import math

a, b = map(int, input().split())

print(math.gcd(a, b)) # 최대공약수
print(math.lcm(a, b)) # 최소공배수

# # 다른 풀이
# a, b = map(int, input().split())

# def gcd(a, b): # 최대공약수
#     while b > 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b): # 최소공배수
#     return a * b // gcd(a, b)

# print(gcd(a, b))
# print(lcm(a, b))