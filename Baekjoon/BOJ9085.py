# 나머지

t = int(input()) # 테스트케이스 개수

for i in range(t):
    nums = [] # 한 줄에 있는 자연수를 담을 리스트
    n = int(input()) # 한 줄에 있는 자연수의 개수
    nums = sum(list(map(int, input().split()))) # 한 줄에 있는 자연수를 리스트에 넣고 sum 함수로 합을 구한다.
    print(nums)