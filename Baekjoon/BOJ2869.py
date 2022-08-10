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
a,b,v = map(int,input().split())
day = (v-b)/(a-b)
print(int(day) if day == int(day) else int(day)+1)