# 여우는 어떻게 울지?
import sys
input = sys.stdin.readline

ano_ani = set()

t = int(input().rstrip())

for i in range(t):

    record = list(map(str, input().rstrip().split()))

    for j in range(100): # 최대 단어 개수 100개

        animal = list(map(str, input().rstrip().split()))

        if animal[0] == "what": # 마지막줄에 what있으면 break
            break
        else:
            ano_ani.add(animal[2]) # 동물의 울음소리

    for k in record:
        if k not in ano_ani: # animal에 없는 동물의 울음소리는 여우소리이다.
            print(k, end=" ")
