from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    input_list = list(map(int, input().split()))

    if input_list[0] == 0: # 0일 때 
        break

    del input_list[0] # k 제거

    input_list = list(combinations(input_list, 6))
    
    for lotto in input_list:
        print(*lotto)
    print()