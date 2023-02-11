# Fly me to the Alpha Centauri

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y-x # 거리
    k = 0

    while True:
        if distance <= k*(k+1):
            break
        k+=1

    if distance <= k**2:
        print(k*2-1)

    else: 
        print(k*2)
    