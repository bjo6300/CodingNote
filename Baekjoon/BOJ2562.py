# 최댓값

lst = []

for _ in range(9):
    lst.append(int(input()))

print(max(lst)) # 리스트에 있는것중 최댓값 구하지
print(lst.index(max(lst))+1) # 인덱스가 0부터 시작하므로 1을 더한다.