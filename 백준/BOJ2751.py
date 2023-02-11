# 수 정렬하기 2
import sys

input = sys.stdin.readline # 이거 안하면 시간초과

N = int(input())

lst = []

for _ in range(N):
    lst.append(int(input())) # lst에 추가

lst.sort() # 오름차순으로 정렬

for i in lst: # lst 출력
    print(i)