# 나머지

lst = []

for _ in range(10):
    x = int(input())
    y = x % 42
    lst.append(y)

print(len(set(lst)))
