# 세 수
lst = list(map(int,input().split()))

lst.remove(max(lst))
print(max(lst))