# 한국이 그리울 땐 서버에 접속하지
import sys

N = int(input().rstrip())
pt = input().rstrip().split("*")
front = len(pt[0]) # 앞쪽 패턴
back = len(pt[1]) # 뒤쪽 패턴

# 앞, 뒤 패턴이 한 문자라는 생각을 버린다.

for i in range(N):
    st = input().rstrip()
    st_front = st[:front] # front의 길이만큼
    st = st[front:] # front를 제거한 나머지 
    st_back = st[len(st) - back :] # 전체 길이 - back 

    if len(st) == 1:
        print("NE")
    elif st_front == pt[0] and st_back == pt[1]:
        print("DA")
    else:
        print("NE")

