# 일반 화학 실험
import sys

input = sys.stdin.readline # 시간 단축

ondo = []

while True:
    temperature = float(input())
    ondo.append(temperature)
    if temperature == 999:
        break
    

i = 0

while True:
    if ondo[i+1] == 999 : break
    print("%.2f" %(ondo[i+1]-ondo[i]))
    i+=1
