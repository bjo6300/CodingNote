# 부분 문자열
## 승훈 풀이
a = input()
b = input()
print(1 if b in a else 0)


# # 시간초과
# import sys
# input = sys.stdin.readline

# s=input().rstrip()
# p = input().rstrip()
# flag = 0

# for i in range(len(s)):
#     for j in range(len(s)):
#         if p == s[i:j]:
#             flag = 1

# print(flag)

# 맞는 코드 (KMP 알고리즘)
# https://landlordgang.tistory.com/82
# def getPI(pattern):
#     j = 0
#     for i in range(1, len(pattern)):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = pi[j - 1]
#         if pattern[i] == pattern[j]:
#             j += 1
#             pi[i] = j

# def KMP(s, pattern):
#     getPI(pattern)
#     j = 0
#     for i in range(len(s)):
#         while j > 0 and s[i] != pattern[j]:
#             j = pi[j - 1]
#         if s[i] == pattern[j]:
#             if j == len(pattern) - 1:
#                 return True
#             else:
#                 j += 1
#     return False

# s = input()
# pattern = input()
# pi = [0 for x in range(len(pattern))]

# if KMP(s, pattern):
#     print('1')
# else:
#     print('0')
