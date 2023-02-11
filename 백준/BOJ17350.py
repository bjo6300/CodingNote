# 2루수 이름이 뭐야

flag = 0

for _ in range(int(input())): # 첫째줄 수만큼 반복
    
    name = input()

    if name == 'anj': # 이름이 'anj'일 때
        flag = 1 # 뭐야;
    
if flag == 1:
    print("뭐야;")
else: # 이름이 'anj'가 아닐 때
    print("뭐야?")
