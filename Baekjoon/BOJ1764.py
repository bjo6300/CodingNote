# 듣보잡

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = []
arr2 = []
for i in range(n): #듣 못
    x = input()
    arr1.append(x)
for i in range(m): #보 못
    y = input()
    arr2.append(y)

answer = list(set(arr1) & set(arr2)) # 듣보잡 교집합
answer.sort()
print(len(answer))
print(''.join(answer), end = '')


# 시간초과
# N, M = map(int,input().split())

# N_list = []
# result = []

# for _ in range(N):
#     N_list.append(input())

# for _ in range(M):
#     a = input()
#     if a in N_list:
#         result.append(a)
    
# print(len(result))
# for j in result:
#     print(j)