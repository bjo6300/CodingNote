# 수 찾기

# 이분탐색
import sys
input = sys.stdin.readline

N = int(input().rstrip())

A = sorted(input().split()) # 이분탐색을 위한 정렬

m = int(input().rstrip())

M = input().split()

for num in M:
    start, end, ans = 0, N-1, False # num을 여러번 찾아야 하니까 for문 안에 선언해야한다.

    while start <= end:

        mid = (start+end) // 2

        if num == A[mid]: # 같으면 1
            ans = True
            print("1")
            break
        elif num > A[mid]: # num이 A[mid]보다 큰 경우
            start = mid + 1 # start를 높인다.
        else: # num이 A[mid]보다 작은 경우
            end = mid - 1 # end를 낮춘다.

    if ans == False:
        print("0")

# set을 이용한 코드
'''
# 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
N = set(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

for i in M:
    if i in N:
        print(1)
    else:
        print(0)
'''
