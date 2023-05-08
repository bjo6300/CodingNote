# a*k-b*(day-1)>=v 이 식을 이항시켜 day>=(v-b)/(a-b)로 만든다.
# day>=(v-b)/(a-b)가 정수가 아닐 경우 +1 시킨다. 
a,b,v = map(int,input().split())
day = (v-b)/(a-b)
#  int(k)와 k가 같다면 k는 (v-b)/(a-b), 다르다면 k는 (v-b)/(a-b)+1이다.
print(int(day) if day == int(day) else int(day)+1)