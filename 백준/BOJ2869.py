# 달팽이는 올라가고 싶다
########## 시간초과
# a,b,v = map(int,input().split()) # 올라감, 내려감, 높이
# day = 0 
# result = 0

# while True:
#     result += a
#     day += 1
#     if result >= v:
#         print(day)
#         break
#     else:
#         result -= b
###########      

# a*k-b*(day-1)>=v 이 식을 이항시켜 day>=(v-b)/(a-b)로 만든다.
# day>=(v-b)/(a-b)가 정수가 아닐 경우 +1 시킨다. 
a,b,v = map(int,input().split())
day = (v-b)/(a-b)
#  int(day)와 day가 같다면 day는 (v-b)/(a-b), 다르다면 day는 (v-b)/(a-b)+1
print(int(day) if day == int(day) else int(day)+1)