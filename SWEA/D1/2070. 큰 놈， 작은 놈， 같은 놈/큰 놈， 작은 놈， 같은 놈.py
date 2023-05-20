t = int(input())

for i in range(1, t + 1):
    x, y = map(int, input().split())

    if x < y:
        print(f"#{i}" + " <")
    elif x == y:
        print(f"#{i}" + " =")
    elif x > y:
        print(f"#{i}" + " >")
