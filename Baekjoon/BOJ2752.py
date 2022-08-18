# 세 수 정렬

import sys

input = sys.stdin.readline

lst = list(map(int, input().rstrip().split())) # int형으로 된 숫자들을 분리 후 리스트안에 넣는다.

print(*sorted(lst)) # *을 이용해 리스트 값을 출력, sorted : 정렬된 상태로 출력