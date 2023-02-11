# 크냐?
import sys

input = sys.stdin.readline # 시간 단축
result = []
while True:
    a,b = map(int,input().split())
    if a==0 | b == 0: 
        break
    if a>b:
        result.append("Yes")
    elif a<=b:
        result.append("No")
    
for i in result:
    print(i)
    