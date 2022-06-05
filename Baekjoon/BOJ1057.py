import sys

input1 = sys.stdin.readline().split()
input1 = list(map(int,input1))
# n,start,end=map(int, input().split()) # 이렇게 바로 변수로 넣는것도 가능

round = 0
# input1[0] = 참가자 수, input1[1] = 김지민 번호. input1[2] = 임한수 번호

while input1[1] != input1[2]:
    input1[1] -= input1[1] // 2  # 그림 그려보고 토너먼트의 특징을 기억하면 이 값이 라운드 수라는걸 알 수 있다.
    input1[2] -= input1[2] // 2  
    round += 1

print(round)

# ex) 8, 9
# 8 -> 4 -> 2 -> 1 -> 1
# 9 -> 5 -> 3 -> 2 -> 1