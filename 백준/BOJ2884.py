# 알람 시계

h,m = map(int,input().split())

if m >= 45 : # 분이 45보다 클 때
    m-=45

elif m<45: # 분이 45보다 작을 때
    m = m + 60 - 45
    if h == 0: # 시간이 00시 일때
        h = 23
    else: # 시간이 0보다 클 때
        h -= 1

print(h, m)