import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
arr = [] 

for _ in range(N):
    arr.append(list(map(int, input().split())))

com = []

for i in range(1, N+1):
    com.append(list(combinations(arr, i))) 

answer = 1000000000
for i in com:
    for j in i: # i는 개수에 따른 조합들, j는 조합들 중 하나
        x = 1 # 곱
        y = 0 # 합
        for z in j: # z는 조합들 중 하나의 리스트
            x *= z[0]
            y += z[1]
        answer = min(answer, abs(x - y))

print(answer)